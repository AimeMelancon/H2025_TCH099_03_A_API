<?php
require_once __DIR__ . '/router.php';
require 'config.php';

require 'api/v1/instructions/getInstructions.php';
require 'api/v1/instructions/getSolution.php';
require 'api/v1/modules/verifyMatricule.php';


get('/api/v1/instructions/$matricule', function ($matricule) {
    getInstructions($matricule);
});

get('/api/v1/solution/$matricule', function ($matricule) {
    getSolution($matricule);
});

get('/api/v1/$modules/$matricule', function ($niveau,$module) {
    verifyMatricule($niveau,$module);
});

get('/api/v1/ordinateur/$niveau', function($niveau) {
    getNiveau($niveau);
});


get('/api/v1/ordinateur/$niveau/$modules', function ($niveau,$module) {
    getModules($niveau,$module);
});


get('/api/v1/web/$module/$matricule', function($module,$matricule){
    getMatricule($module,$matricule);
})

?>