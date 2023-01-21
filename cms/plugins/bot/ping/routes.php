<?php

use Bot\Ping\Http\Controllers\MessageController;

Route::group(['prefix' => 'api'], function () {
    Route::group(['prefix' => 'v1'], function () {
        Route::group(['prefix' => 'ping'], function () {
            Route::get('/', [MessageController::class, 'index']);
            Route::get('/{type}', [MessageController::class, 'message']);
        });
    });
});
