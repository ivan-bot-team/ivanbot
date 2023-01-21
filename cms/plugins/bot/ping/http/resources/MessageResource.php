<?php

namespace Bot\Ping\Http\Resources;

use \Illuminate\Http\Resources\Json\JsonResource;

class MessageResource extends JsonResource
{
    public function toArray($request)
    {
        return [
            'message' => $this->message,
        ];
    }
}
