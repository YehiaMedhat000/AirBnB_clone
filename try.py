    def default(self, line):
        """ Override for the default method
            to handle the dot notation

        Args:
            line -- The line passed to the command
            self -- The cmd object
        """

        if '.' in line and line[-1] == ')':
            args = line.split('.')
            cmd, arg = args[1], args[0]
            args = " ".join([cmd[:-2], arg])
            self.onecmd(args)
        else:
            self.stdout.write('*** Unknown syntax: %s\n'%line)
