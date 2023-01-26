<?php

use Bot\Process\Http\Controllers\ProcessController;

Route::group(['prefix' => 'api'], function () {
    Route::group(['prefix' => 'v1'], function () {
        Route::group(['prefix' => 'process'], function () {
                Route::get('/start', [ProcessController::class, 'start']);
                Route::get('/stop', [ProcessController::class, 'stop']);
                Route::get('/reset', [ProcessController::class, 'reset']);
        });
    });
});
