<?php namespace Bot\Config;

use Backend;
use System\Classes\PluginBase;

/**
 * config Plugin Information File
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
            'name'        => 'config',
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
            'Bot\Config\Components\MyComponent' => 'myComponent',
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
            'bot.config.some_permission' => [
                'tab' => 'config',
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
            'config' => [
                'label'       => 'Config',
                'url'         => Backend::url('bot/config/guilds'),
                'icon'        => 'icon-leaf',
                'permissions' => ['bot.config.*'],
                'order'       => 500,
                'sideMenu' => [
                    'groups' => [
                        'label'       => 'Guilds',
                        'icon'        => 'icon-leaf',
                        'url'         => Backend::url('bot/config/guilds'),
                        'permissions' => ['bot.config.*'],
                    ],
                ]
            ],
        ];
    }

    public function registerSettings()
    {
        return [
            'bot_settings' => [
                'label'       => 'Bot Settings',
                'description' => 'Manage user based settings.',
                'category'    => 'Bot',
                'icon'        => 'icon-cog',
                'class'       => 'Bot\Config\Models\Config',
                'order'       => 500,
                'keywords'    => 'bot',
            ]
        ];
    }
}
