<?php

namespace Bot\Config\Http\Controllers;

use Illuminate\Routing\Controller;
use Bot\Config\Http\Resources\ConfigResource as Resource;
use Bot\Config\Models\Config;

use Bot\Config\Classes\Config as ConfigClass;

class ConfigController extends Controller
{
    public function index(): Resource
    {
        return Resource::make(new ConfigClass);
    }

}
