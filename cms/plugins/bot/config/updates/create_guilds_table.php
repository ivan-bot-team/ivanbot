<?php namespace Bot\Config\Updates;

use Schema;
use October\Rain\Database\Schema\Blueprint;
use October\Rain\Database\Updates\Migration;

class CreateGuildsTable extends Migration
{
    public function up()
    {
        Schema::create('bot_config_guilds', function (Blueprint $table) {
            $table->engine = 'InnoDB';
            $table->increments('id');
            $table->string('name')->nullable();
            $table->string('description')->nullable();
            $table->bigInteger('guild_id');
            $table->integer('config_id')->default(1);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('bot_config_guilds');
    }
}
