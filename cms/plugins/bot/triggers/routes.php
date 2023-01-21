<?php

use Bot\Triggers\Http\Controllers\TriggerController;

Route::group(['prefix' => 'api'], function () {
    Route::group(['prefix' => 'v1'], function () {
        Route::group(['prefix' => 'triggers'], function () {
            Route::get('/', [TriggerController::class, 'index']);
            Route::get('/{message}', [TriggerController::class, 'search']);
        });
    });
});

