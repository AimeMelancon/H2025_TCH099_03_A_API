<?php

function getMatricule($module,$matricule)
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

    
   

    try {
        //Préparation de la requête sql.
        $req = $pdo->prepare(
            'SELECT matricule = :matricule
                    FROM   module = :module'
        );
        //L'association des variable sql avec les variables de la requêtes
        $req->execute([
            "matricule" => $matricule,
            "module"    => $module
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