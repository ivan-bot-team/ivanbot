<?php

namespace Bot\Ping\Http\Controllers;

use Illuminate\Routing\Controller;
use Bot\Ping\Http\Resources\MessageResource as Resource;
use Bot\Ping\Models\Message;

class MessageController extends Controller
{
    public function index(): \Illuminate\Http\Resources\Json\AnonymousResourceCollection
    {
        return Resource::collection(Message::all());
    }

    public function message($type): \Illuminate\Http\Resources\Json\AnonymousResourceCollection
    {
        return Resource::collection(Message::where('type', $type)->get());
    }
}
