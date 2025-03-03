<?php 
require_once __DIR__ . '/router.php';
require 'config.php';

require 'api/v1/instructions/getInstructions.php';
require 'api/v1/instructions/getSolution.php';


get('/api/v1/instructions/$matricule', function () {
    getInstructions();
    });

get('/api/v1/solution/$matricule', function () {
    getSolution();
    });    



?>