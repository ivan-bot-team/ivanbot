<?php

namespace Bot\Config\Classes;

use Bot\Config\Models\Config as Model;
use Bot\Cogs\Models\Cog;
use Bot\Status\Models\Message;
use Bot\Config\Models\Guild;
use Bot\Ping\Models\Channel;

class Config
{
    public $string_similiraty;
    public $cogs;
    public $status_freq;
    public $status_messages;
    public $guilds;
    public $ping_freq_random;
    public $ping_freq_target;
    public $ping_channels;

    public function __construct()
    {
        $this->string_similiraty = Model::get('string_similarity');
        $this->cogs = Cog::where('enabled', true)->get();
        $this->status_freq = Model::get('status_freq');
        $this->status_messages = Message::all();
        $this->guilds = Guild::all();
        $this->ping_freq_random = Model::get('ping_freq_random');
        $this->ping_freq_target = Model::get('ping_freq_target');
        $this->ping_channels = Channel::all();
    }
}
