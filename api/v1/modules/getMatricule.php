<?php

function getMatricule()
{

    // Ajout des headers requis
    header('Access-Control-Allow-Origin: *');
    header("Content-Type: application/json; charset=utf-8");

    //La variable super global pdo
    global $pdo;

    // La seule méthode autorisée est GET
    if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
        http_response_code(405);
        echo json_encode(["error" => "Methode HTTP non autorisée"]);
        exit();
    }


    //On cherche les informations usr la requête
    preg_match('/\/api\/v([0-9]+)\/web\/([A-Za-z0-9]+)\/([A-Za-z0-9]+)/', $_SERVER['REQUEST_URI'], $matches);

    // Vérification que la route contienne la version de l'API ($matches[1]) et un matricule ($matches[2]) .
    if (!isset($matches[1]) || !isset($matches[2]) || !isset($matches[3])) {
        http_response_code(400);
        echo json_encode(["error" => "Route invalide"]);
        exit();
    }

    //Assignation des variables de la requête
    $api_version = $matches[1];
    $module = $matches[2];
    $matricule = $matches[3];

    try {
        //Préparation de la requête sql.
        $req = $pdo->prepare(
            'SELECT matricule = :matricule
                    FROM   module = :module
                    WHERE api_ver = :api_ver'
        );
        //L'association des variable sql avec les variables de la requêtes
        $req->execute([
            "matricule" => $matricule,
            "module"    => $module,
            "api_ver"   => $api_version
        ]);

        $rep = $req->fetchAll(PDO::FETCH_ASSOC);


        //On vérifie si la requête à bien fonctionné.
        if($rep){
            echo json_encode($rep, JSON_PRETTY_PRINT);
        }else{
            http_response_code(204);
            echo json_encode([
                "error"=> "Aucun des modules possède se matricule."
            ]);
        }

    } catch (Exception $e) {
        //On attrape l'erreur et on l'affiche.
        http_response_code(404);
        echo json_encode([
            "error" => $e->getMessage()
        ]);

    }


}
?>