<?php 
function getSolution() {
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

    
    preg_match('/\/api\/v([0-9]+)\/solution\/([A-Za-z0-9]+)/', $_SERVER['REQUEST_URI'], $matches);

    // Vérification que la route contienne la version de l'API ($matches[1]) et un matricule ($matches[2]) 
    if (!isset($matches[1]) || !isset($matches[2])) {
        http_response_code(400);
        echo json_encode(["error" => "Route invalide"]);
        exit();
    }    

    $api_version = $matches[1];
    $matricule = $matches[2];


    // Requête PLACEHOLDER; vraie requête à venir
    $query = 
    "SELECT solution_text
    FROM Solutions
    WHERE matricule = :mat AND api_ver = :api_ver
    ";



    // Exécuter la requête SQL avec paramètres la version d'api et le matricule
    $stmt = $pdo->prepare($query);
    $stmt->bindParam(":mat", $matricule);
    $stmt->bindParam("api_ver", $api_version);
    $stmt->execute();
    $result = $stmt->fetchAll();

    // Envoyer la solution (ou une erreur si cela n'a pas fonctionné)
    if ($result) {
        http_response_code(200);
        echo json_encode($result);
    } else {
        http_response_code(404);
        echo json_encode(["error" => "Solution non trouvée"]);
    }


}


?>