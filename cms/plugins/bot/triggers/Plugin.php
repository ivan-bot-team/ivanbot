<?php namespace Bot\Triggers;

use Backend;
use System\Classes\PluginBase;

/**
 * triggers Plugin Information File
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
            'name'        => 'triggers',
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
            'Bot\Triggers\Components\MyComponent' => 'myComponent',
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
            'bot.triggers.some_permission' => [
                'tab' => 'triggers',
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
            'triggers' => [
                'label'       => 'Trigger Groups',
                'url'         => Backend::url('bot/triggers/groups'),
                'icon'        => 'icon-leaf',
                'permissions' => ['bot.triggers.*'],
                'order'       => 500,
                'sideMenu' => [
                    'groups' => [
                        'label'       => 'Trigger Groups',
                        'icon'        => 'icon-leaf',
                        'url'         => Backend::url('bot/triggers/groups'),
                        'permissions' => ['bot.triggers.*'],
                    ],
                    'keywords' => [
                        'label'       => 'Keywords',
                        'icon'        => 'icon-leaf',
                        'url'         => Backend::url('bot/triggers/keywords'),
                        'permissions' => ['bot.triggers.*'],
                    ],
                    'triggers' => [
                        'label'       => 'Messages',
                        'icon'        => 'icon-leaf',
                        'url'         => Backend::url('bot/triggers/messages'),
                        'permissions' => ['bot.triggers.*'],
                    ],
                ]
            ],
        ];
    }
}
