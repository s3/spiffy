def rehash(self, input): 
    """Reloads the configuration for the current network, for use by admins only.""" 
    if not input.isowner():
        self.say('This command is for admins only.')
        return

    s = lambda x: '' if len(x) == 1 else 's'

    if input.args == '-v':
        verbose = True
    else:
        verbose = False

    
    info = self.bot.rehash()
    if info == False:
        self.say('Error: Unable to rehash, config.py is missing.')
        return
    
    if verbose:
        if info['settings']['added']:
            self.say('Added \x02%s\x02 new setting%s:' % (len(info['settings']['added']), s(info['settings']['added'])))
            for setting in info['settings']['added']:
                self.say(" + '%s': %s" % setting)

        if info['settings']['removed']:
            self.say('Removed \x02%s\x02 setting%s:' % (len(info['settings']['removed']), s(info['settings']['removed'])))
            for setting in info['settings']['removed']:
                self.say(" - '%s'" % setting)

        if info['settings']['changed']:
            self.say('Changed \x02%s\x02 setting%s:' % (len(info['settings']['changed']), s(info['settings']['changed'])))
            for setting in info['settings']['changed']:
                self.say(" * '%s': %s \x02->\x02 %s" % setting)
        
        if info['plugins']['added']:
            self.say('Loaded \x02%s\x02 new plugin%s:' % (len(info['plugins']['added']), s(info['plugins']['added'])))
            self.say(", ".join(info['plugins']['added']))

        if info['plugins']['removed']:
            self.say('Removed \x02%s\x02 plugin%s:' % (len(info['plugins']['removed']), s(info['plugins']['removed'])))
            self.say(", ".join(info['plugins']['removed']))    

    self.say('Configuration successfully reloaded!')
        
rehash.rule = ['rehash']
rehash.usage = [("Reload the configuration and all plugins", "$pcmd"),
    ("Verbose version of the command above", "$pcmd -v")]
