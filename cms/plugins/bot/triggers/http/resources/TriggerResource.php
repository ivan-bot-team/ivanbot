<?php

namespace Bot\Triggers\Http\Resources;

use \Illuminate\Http\Resources\Json\JsonResource;

class TriggerResource extends JsonResource
{
    public function toArray($request): array
    {
        return [
            'message' => $this->message,
        ];
    }
}
