<?php 
function getInstructions($matricule) {
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




    // Requête PLACEHOLDER; vraie requête à venir
    $query = 
    "SELECT instruction_text
    FROM Instructions
    WHERE matricule = :mat
    ";



    // Exécuter la requête SQL avec paramètres la version d'api et le matricule
    $stmt = $pdo->prepare($query);
    $stmt->bindParam(":mat", $matricule);
    $stmt->execute();
    $result = $stmt->fetchAll();

    // Envoyer les instructions (ou une erreur si cela n'a pas fonctionné)
    if ($result) {
        http_response_code(200);
        echo json_encode($result);
    } else {
        http_response_code(404);
        echo json_encode(["error" => "Instructions non trouvées"]);
    }


}


?>