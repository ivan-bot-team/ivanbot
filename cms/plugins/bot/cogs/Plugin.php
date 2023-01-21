<?php namespace Bot\Cogs;

use Backend;
use System\Classes\PluginBase;

/**
 * cogs Plugin Information File
 */
class Plugin extends PluginBase
{
    /**
     * Returns information about this plugin.
     *
     * @return array
     */
    public function pluginDetails()
    {
        return [
            'name'        => 'cogs',
            'description' => 'No description provided yet...',
            'author'      => 'bot',
            'icon'        => 'icon-leaf'
        ];
    }

    /**
     * Register method, called when the plugin is first registered.
     *
     * @return void
     */
    public function register()
    {

    }

    /**
     * Boot method, called right before the request route.
     *
     * @return array
     */
    public function boot()
    {

    }

    /**
     * Registers any front-end components implemented in this plugin.
     *
     * @return array
     */
    public function registerComponents()
    {
        return []; // Remove this line to activate

        return [
            'Bot\Cogs\Components\MyComponent' => 'myComponent',
        ];
    }

    /**
     * Registers any back-end permissions used by this plugin.
     *
     * @return array
     */
    public function registerPermissions()
    {
        return []; // Remove this line to activate

        return [
            'bot.cogs.some_permission' => [
                'tab' => 'cogs',
                'label' => 'Some permission'
            ],
        ];
    }

    /**
     * Registers back-end navigation items for this plugin.
     *
     * @return array
     */
    public function registerNavigation()
    {
        return [
            'cogs' => [
                'label'       => 'Cogs',
                'url'         => Backend::url('bot/cogs/cogs'),
                'icon'        => 'icon-leaf',
                'permissions' => ['bot.cogs.*'],
                'order'       => 500,
            ],
        ];
    }
}
