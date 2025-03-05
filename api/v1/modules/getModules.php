<?php
function getModules()
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
    preg_match('/\/api\/v([0-9]+)\/ordinateur\/([A-Za-z0-9]+)\/([A-Za-z0-9]+)/', $_SERVER['REQUEST_URI'], $matches);

    // Vérification que la route contienne la version de l'API ($matches[1]) et un matricule ($matches[2]) .
    if (!isset($matches[1]) || !isset($matches[2])|| !isset($matches[3])) {
        http_response_code(400);
        echo json_encode(["error" => "Route invalide"]);
        exit();
    }

    //Assignation de variable
    $api_version = $matches[1];
    $niveau = $matches[2];
    $module = $matches[3];
    //Permet de créer un champ pour savoir si le sql va bien s'effectuer ou non
    try {
        //Préparation de la requête sql. 
        //TODO: Vérifié le sql écrit, car je ne suis pas sûr de ce que j'ai fait.
        $req = $pdo->prepare
        ('SELECT module.*
             FROM niveau =:niveau
             JOIN module ON module.id_module = :id_module
             WHERE api_ver = :api_ver AND module.id_module = :id_module
    ');

        //Association des paramètres reçu avec les paramètres sql. 
        $req->execute([
            "api_ver" => $api_version,
            "id_module" => $module,
            "niveau" => $niveau
        ]);

        //On envoie la requête
        $rep = $req->fetchAll(PDO::FETCH_ASSOC);

        //On vérifie si la requête à bien fonctionner
        if ($rep) {
            echo json_encode($rep, JSON_PRETTY_PRINT);
        } else {
            http_response_code(204);
            echo json_encode(["error" => "Aucun des modules ne possède cet id."]);
        }

        //Si la requête est attrapé ça veut dire 
    } catch (Exception $e) {
        http_response_code(404);
        echo json_encode(["error" => $e->getMessage()]);
    }


}
?>