<?php

use Bot\Config\Http\Controllers\ConfigController;

Route::group(['prefix' => 'api'], function () {
    Route::group(['prefix' => 'v1'], function () {
        Route::group(['prefix' => 'bot'], function () {
            Route::group(['prefix' => 'config'], function () {
                Route::get('/', [ConfigController::class, 'index']);
            });
        });
    });
});
