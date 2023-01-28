<?php namespace Bot\Triggers\Updates;

use Schema;
use October\Rain\Database\Schema\Blueprint;
use October\Rain\Database\Updates\Migration;

class CreateKeywordsTable extends Migration
{
    public function up()
    {
        Schema::create('bot_triggers_keywords', function (Blueprint $table) {
            $table->engine = 'InnoDB';
            $table->increments('id');
            $table->integer('group_id')->unsigned()->nullable();
            $table->text('keyword')->fulltext();
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('bot_triggers_keywords');
    }
}
