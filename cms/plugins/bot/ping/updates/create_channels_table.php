<?php namespace Bot\Ping\Updates;

use Schema;
use October\Rain\Database\Schema\Blueprint;
use October\Rain\Database\Updates\Migration;

class CreateChannelsTable extends Migration
{
    public function up()
    {
        Schema::create('bot_ping_channels', function (Blueprint $table) {
            $table->engine = 'InnoDB';
            $table->increments('id');
            $table->string('name');
            $table->bigInteger('channel_id');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('bot_ping_channels');
    }
}
