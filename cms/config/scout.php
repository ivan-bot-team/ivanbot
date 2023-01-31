<?php

return [
    'driver' => env('SCOUT_DRIVER', 'mysql'),
    'prefix' => env('SCOUT_PREFIX', ''),
    'queue' => false,
    'mysql' => [
        'mode' => 'NATURAL_LANGUAGE',
        'model_directories' => [app_path()],
        'min_search_length' => 0,
        'min_fulltext_search_length' => 1,
        'min_fulltext_search_fallback' => 'LIKE',
        'query_expansion' => true
    ]
];
