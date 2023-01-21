<?php namespace Bot\Cogs\Updates;

use Schema;
use October\Rain\Database\Schema\Blueprint;
use October\Rain\Database\Updates\Migration;

class CreateCogsTable extends Migration
{
    public function up()
    {
        Schema::create('bot_cogs_cogs', function (Blueprint $table) {
            $table->engine = 'InnoDB';
            $table->increments('id');
            $table->string('name');
            $table->string('description');
            $table->string('filename');
            $table->boolean('enabled')->default(0);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('bot_cogs_cogs');
    }
}
