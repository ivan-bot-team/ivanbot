<?php

namespace Bot\Triggers\Http\Controllers;

use Illuminate\Routing\Controller;
use October\Rain\Exception\ApplicationException;
use Bot\Triggers\Http\Resources\TriggerResource as Resource;
use Bot\Triggers\Models\Keyword;
use Bot\Triggers\Models\Message;

class TriggerController extends Controller
{
    public function index(): \Illuminate\Http\Resources\Json\AnonymousResourceCollection
    {
        return Resource::collection(Message::all());
    }

    public function search()
    {
        $message = get('message');
        $words = explode(' ', $message);
        foreach ($words as $word) {
            $keyword = Keyword::search($word)->orderBy("relevance")->get();
            if ($keyword->count() > 0) {
                return Resource::collection(Message::where('group_id', $keyword[0]->group_id)->get());
            }
        }

        throw new ApplicationException('nonefound');
    }
}
