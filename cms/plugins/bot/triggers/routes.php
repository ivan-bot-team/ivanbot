<?php

use Bot\Triggers\Http\Controllers\TriggerController;

Route::group(['prefix' => 'api'], function () {
    Route::group(['prefix' => 'v1'], function () {
        Route::group(['prefix' => 'bot'], function () {
            Route::group(['prefix' => 'triggers'], function () {
                Route::get('/', [TriggerController::class, 'index']);
                Route::get('/search', [TriggerController::class, 'search']);
            });
        });
    });
});
