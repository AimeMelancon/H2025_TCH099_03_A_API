<?php

function verifyMatricule($niveau,$module) {
    // Ajout des headers requis
    header('Access-Control-Allow-Origin: *');
    header("Content-Type: application/json");

    
    global $pdo;

    // La seule méthode autorisée est GET
    if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
        http_response_code(405);
        echo json_encode(["error" => "Methode HTTP non autorisée"]);
        exit();
        }

        //TODO: À retirer pour mettre le code qui le complète.
    echo $niveau."  ".$module;
    
    // continuer...

}



?>