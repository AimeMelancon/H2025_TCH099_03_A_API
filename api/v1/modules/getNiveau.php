<?php
function getNiveau($niveau)
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
    

    //Assignation de variable
    $niv = $niveau;

    //Permet de créer un champ pour savoir si le sql va bien s'effectuer ou non
    try {
        //Préparation de la requête sql.
        $req = $pdo->prepare
        ('SELECT *
                 FROM niveau');

        //Association des paramètres reçu avec les paramètres sql.
        $req->execute([
            "id_niv" => $niv
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