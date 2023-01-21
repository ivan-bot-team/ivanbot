<?php namespace Bot\Ping;

use Backend;
use System\Classes\PluginBase;

/**
 * ping Plugin Information File
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
            'name'        => 'ping',
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
            'Bot\Ping\Components\MyComponent' => 'myComponent',
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
            'bot.ping.some_permission' => [
                'tab' => 'ping',
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
            'ping' => [
                'label'       => 'Ping',
                'url'         => Backend::url('bot/ping/channels'),
                'icon'        => 'icon-leaf',
                'permissions' => ['bot.ping.*'],
                'order'       => 500,
                'sideMenu' => [
                    'channels' => [
                        'label'       => 'Channels',
                        'icon'        => 'icon-leaf',
                        'url'         => Backend::url('bot/ping/channels'),
                        'permissions' => ['bot.ping.*'],
                    ],
                    'messages' => [
                        'label'       => 'Messages',
                        'icon'        => 'icon-leaf',
                        'url'         => Backend::url('bot/ping/messages'),
                        'permissions' => ['bot.ping.*'],
                    ],
                ]
            ],
        ];
    }
}
