<?php

namespace Bot\Triggers\Http\Controllers;

use Illuminate\Routing\Controller;
use Bot\Triggers\Http\Resources\TriggerResource as Resource;
use Bot\Triggers\Models\Keyword;
use Bot\Triggers\Models\Message;

class TriggerController extends Controller
{
    public function index(): \Illuminate\Http\Resources\Json\AnonymousResourceCollection
    {
        return Resource::collection(Message::all());
    }

    public function search($message): \Illuminate\Http\Resources\Json\AnonymousResourceCollection
    {
        return Resource::collection(
            Message::where('group_id', Keyword::search($message)->get()[0]->group_id)->get()
        );
    }
}
