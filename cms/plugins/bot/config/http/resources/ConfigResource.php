<?php

namespace Bot\Config\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;

class ConfigResource extends JsonResource
{
    public function toArray($request)
    {
        return [
            'bot_token' => $this->bot_token,
            'cogs' => $this->cogs,
            'status_freq' => $this->status_freq,
            'status_messages' => $this->status_messages,
            'guilds' => $this->guilds,
            'ping_freq_random' => $this->ping_freq_random,
            'ping_freq_target' => $this->ping_freq_target,
            'ping_channels' => $this->ping_channels,
        ];
    }
}
