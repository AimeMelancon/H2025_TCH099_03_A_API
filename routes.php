<?php
require_once __DIR__ . '/router.php';
require 'config.php';

require 'api/v1/instructions/getInstructions.php';
require 'api/v1/instructions/getSolution.php';
require 'api/v1/modules/verifyMatricule.php';


get('/api/v1/instructions/$matricule', function () {
    getInstructions();
});

get('/api/v1/solution/$matricule', function () {
    getSolution();
});

get('/api/v1/$modules/$matricule', function () {
    verifyMatricule();
});

get('/api/v1/ordinateur/$niveau', function() {
    getNiveau();
});


get('/api/v1/ordinateur/$niveau/$modules', function () {
    getModules();
});

?>