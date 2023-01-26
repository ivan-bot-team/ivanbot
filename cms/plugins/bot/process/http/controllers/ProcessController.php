<?php namespace Bot\Process\Http\Controllers;

use Illuminate\Routing\Controller;

class ProcessController extends Controller
{

    public static function start()
    {
        $dir = shell_exec('pwd');
        return $dir;
    }

    public static function stop()
    {
    }

    public static function reset()
    {
    }
}
