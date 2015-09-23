# coding=utf-8
__author__ = 'Administrator'


class Widget():
    pass

class XView():
    pass

class YView():
    pass


# 继承自Widget
class Text(Widget, XView, YView):
    """Text widget which can display text in various forms."""
    def __init__(self, master=None, cnf={}, **kw):
        """Construct a text widget with the parent MASTER.

        STANDARD OPTIONS

            background, borderwidth, cursor,
            exportselection, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, insertbackground,
            insertborderwidth, insertofftime,
            insertontime, insertwidth, padx, pady,
            relief, selectbackground,
            selectborderwidth, selectforeground,
            setgrid, takefocus,
            xscrollcommand, yscrollcommand,

        WIDGET-SPECIFIC OPTIONS

            autoseparators, height, maxundo,
            spacing1, spacing2, spacing3,
            state, tabs, undo, width, wrap,

        """
        Widget.__init__(self, master, 'text', cnf, kw)

    def bbox(self, *args):
        """Return a tuple of (x,y,width,height) which gives the bounding
        box of the visible part of the character at the index in ARGS."""
        return self._getints(self.tk.call((self._w, 'bbox') + args)) or None

    def tk_textSelectTo(self, index):
        self.tk.call('tk_textSelectTo', self._w, index)

    def tk_textBackspace(self):
        self.tk.call('tk_textBackspace', self._w)

    def tk_textIndexCloser(self, a, b, c):
        self.tk.call('tk_textIndexCloser', self._w, a, b, c)

    def tk_textResetAnchor(self, index):
        self.tk.call('tk_textResetAnchor', self._w, index)
    def compare(self, index1, op, index2):
        """Return whether between index INDEX1 and index INDEX2 the
        relation OP is satisfied. OP is one of <, <=, ==, >=, >, or !=."""
        return self.tk.getboolean(self.tk.call(
            self._w, 'compare', index1, op, index2))
    def debug(self, boolean=None):
        """Turn on the internal consistency checks of the B-Tree inside the text
        widget according to BOOLEAN."""
        if boolean is None:
            return self.tk.getboolean(self.tk.call(self._w, 'debug'))
        self.tk.call(self._w, 'debug', boolean)
    def delete(self, index1, index2=None):
        """Delete the characters between INDEX1 and INDEX2 (not included)."""
        self.tk.call(self._w, 'delete', index1, index2)
    def dlineinfo(self, index):
        """Return tuple (x,y,width,height,baseline) giving the bounding box
        and baseline position of the visible part of the line containing
        the character at INDEX."""
        return self._getints(self.tk.call(self._w, 'dlineinfo', index))
    def dump(self, index1, index2=None, command=None, **kw):
        """Return the contents of the widget between index1 and index2.

        The type of contents returned in filtered based on the keyword
        parameters; if 'all', 'image', 'mark', 'tag', 'text', or 'window' are
        given and true, then the corresponding items are returned. The result
        is a list of triples of the form (key, value, index). If none of the
        keywords are true then 'all' is used by default.

        If the 'command' argument is given, it is called once for each element
        of the list of triples, with the values of each triple serving as the
        arguments to the function. In this case the list is not returned."""
        args = []
        func_name = None
        result = None
        if not command:
            # Never call the dump command without the -command flag, since the
            # output could involve Tcl quoting and would be a pain to parse
            # right. Instead just set the command to build a list of triples
            # as if we had done the parsing.
            result = []
            def append_triple(key, value, index, result=result):
                result.append((key, value, index))
            command = append_triple
        try:
            if not isinstance(command, str):
                func_name = command = self._register(command)
            args += ["-command", command]
            for key in kw:
                if kw[key]: args.append("-" + key)
            args.append(index1)
            if index2:
                args.append(index2)
            self.tk.call(self._w, "dump", *args)
            return result
        finally:
            if func_name:
                self.deletecommand(func_name)

    ## new in tk8.4
    def edit(self, *args):
        """Internal method

        This method controls the undo mechanism and
        the modified flag. The exact behavior of the
        command depends on the option argument that
        follows the edit argument. The following forms
        of the command are currently supported:

        edit_modified, edit_redo, edit_reset, edit_separator
        and edit_undo

        """
        return self.tk.call(self._w, 'edit', *args)

    def edit_modified(self, arg=None):
        """Get or Set the modified flag

        If arg is not specified, returns the modified
        flag of the widget. The insert, delete, edit undo and
        edit redo commands or the user can set or clear the
        modified flag. If boolean is specified, sets the
        modified flag of the widget to arg.
        """
        return self.edit("modified", arg)

    def edit_redo(self):
        """Redo the last undone edit

        When the undo option is true, reapplies the last
        undone edits provided no other edits were done since
        then. Generates an error when the redo stack is empty.
        Does nothing when the undo option is false.
        """
        return self.edit("redo")

    def edit_reset(self):
        """Clears the undo and redo stacks
        """
        return self.edit("reset")

    def edit_separator(self):
        """Inserts a separator (boundary) on the undo stack.

        Does nothing when the undo option is false
        """
        return self.edit("separator")

    def edit_undo(self):
        """Undoes the last edit action

        If the undo option is true. An edit action is defined
        as all the insert and delete commands that are recorded
        on the undo stack in between two separators. Generates
        an error when the undo stack is empty. Does nothing
        when the undo option is false
        """
        return self.edit("undo")

    def get(self, index1, index2=None):
        """Return the text from INDEX1 to INDEX2 (not included)."""
        return self.tk.call(self._w, 'get', index1, index2)
        # (Image commands are new in 8.0)

    def image_cget(self, index, option):
        """Return the value of OPTION of an embedded image at INDEX."""
        if option[:1] != "-":
            option = "-" + option
        if option[-1:] == "_":
            option = option[:-1]
        return self.tk.call(self._w, "image", "cget", index, option)

    def image_configure(self, index, cnf=None, **kw):
        """Configure an embedded image at INDEX."""
        return self._configure(('image', 'configure', index), cnf, kw)
    def image_create(self, index, cnf={}, **kw):
        """Create an embedded image at INDEX."""
        return self.tk.call(
            self._w, "image", "create", index,
            *self._options(cnf, kw))
    def image_names(self):
        """Return all names of embedded images in this widget."""
        return self.tk.call(self._w, "image", "names")

    def index(self, index):
        # 形式：line.char
        """Return the index in the form line.char for INDEX."""
        return str(self.tk.call(self._w, 'index', index))

    def insert(self, index, chars, *args):
        """Insert CHARS before the characters at INDEX. An additional
        tag can be given in ARGS. Additional CHARS and tags can follow in ARGS."""
        self.tk.call((self._w, 'insert', index, chars) + args)

    def mark_gravity(self, markName, direction=None):
        """Change the gravity of a mark MARKNAME to DIRECTION (LEFT or RIGHT).
        Return the current value if None is given for DIRECTION."""
        return self.tk.call(
            (self._w, 'mark', 'gravity', markName, direction))

    def mark_names(self):
        """Return all mark names."""
        return self.tk.splitlist(self.tk.call(
            self._w, 'mark', 'names'))

    def mark_set(self, markName, index):
        """Set mark MARKNAME before the character at INDEX."""
        self.tk.call(self._w, 'mark', 'set', markName, index)

    def mark_unset(self, *markNames):
        """Delete all marks in MARKNAMES."""
        self.tk.call((self._w, 'mark', 'unset') + markNames)

    def mark_next(self, index):
        """Return the name of the next mark after INDEX."""
        return self.tk.call(self._w, 'mark', 'next', index) or None

    def mark_previous(self, index):
        """Return the name of the previous mark before INDEX."""
        return self.tk.call(self._w, 'mark', 'previous', index) or None

    def scan_mark(self, x, y):
        """Remember the current X, Y coordinates."""
        self.tk.call(self._w, 'scan', 'mark', x, y)
    def scan_dragto(self, x, y):
        """Adjust the view of the text to 10 times the
        difference between X and Y and the coordinates given in
        scan_mark."""
        self.tk.call(self._w, 'scan', 'dragto', x, y)

    def search(self, pattern, index, stopindex=None,
               forwards=None, backwards=None, exact=None,
               regexp=None, nocase=None, count=None, elide=None):
        """Search PATTERN beginning from INDEX until STOPINDEX.
        Return the index of the first character of a match or an
        empty string."""
        args = [self._w, 'search']

        if forwards: args.append('-forwards')
        if backwards: args.append('-backwards')
        if exact: args.append('-exact')
        if regexp: args.append('-regexp')
        if nocase: args.append('-nocase')
        if elide: args.append('-elide')

        if count: args.append('-count'); args.append(count)

        if pattern and pattern[0] == '-': args.append('--')
        args.append(pattern)
        args.append(index)
        if stopindex: args.append(stopindex)
        return str(self.tk.call(tuple(args)))

    def see(self, index):
        """Scroll such that the character at INDEX is visible."""
        self.tk.call(self._w, 'see', index)

    def tag_add(self, tagName, index1, *args):
        """Add tag TAGNAME to all characters between INDEX1 and index2 in ARGS.
        Additional pairs of indices may follow in ARGS."""
        self.tk.call((self._w, 'tag', 'add', tagName, index1) + args)

    def tag_unbind(self, tagName, sequence, funcid=None):
        """Unbind for all characters with TAGNAME for event SEQUENCE  the
        function identified with FUNCID."""
        self.tk.call(self._w, 'tag', 'bind', tagName, sequence, '')
        if funcid:
            self.deletecommand(funcid)

    def tag_bind(self, tagName, sequence, func, add=None):
        """Bind to all characters with TAGNAME at event SEQUENCE a call to function FUNC.

        An additional boolean parameter ADD specifies whether FUNC will be
        called additionally to the other bound function or whether it will
        replace the previous function. See bind for the return value."""
        return self._bind((self._w, 'tag', 'bind', tagName),
                          sequence, func, add)
    def tag_cget(self, tagName, option):
        """Return the value of OPTION for tag TAGNAME."""
        if option[:1] != '-':
            option = '-' + option
        if option[-1:] == '_':
            option = option[:-1]
        return self.tk.call(self._w, 'tag', 'cget', tagName, option)
    def tag_configure(self, tagName, cnf=None, **kw):
        """Configure a tag TAGNAME."""
        return self._configure(('tag', 'configure', tagName), cnf, kw)
    tag_config = tag_configure
    def tag_delete(self, *tagNames):
        """Delete all tags in TAGNAMES."""
        self.tk.call((self._w, 'tag', 'delete') + tagNames)
    def tag_lower(self, tagName, belowThis=None):
        """Change the priority of tag TAGNAME such that it is lower
        than the priority of BELOWTHIS."""
        self.tk.call(self._w, 'tag', 'lower', tagName, belowThis)

    def tag_names(self, index=None):
        """Return a list of all tag names."""
        return self.tk.splitlist(
            self.tk.call(self._w, 'tag', 'names', index))

    def tag_nextrange(self, tagName, index1, index2=None):
        """
        返回一个start 和 end
        Return a list of start and end index for the first sequence of
        characters between INDEX1 and INDEX2

        which all have tag TAGNAME.
        The text is searched forward from INDEX1.
        """
        return self.tk.splitlist(self.tk.call(
            self._w, 'tag', 'nextrange', tagName, index1, index2))

    def tag_prevrange(self, tagName, index1, index2=None):
        """Return a list of start and end index for the first sequence of
        characters between INDEX1 and INDEX2 which all have tag TAGNAME.
        The text is searched backwards from INDEX1.
        """
        return self.tk.splitlist(self.tk.call(
            self._w, 'tag', 'prevrange', tagName, index1, index2))

    def tag_raise(self, tagName, aboveThis=None):
        """Change the priority of tag TAGNAME such that it is higher
        than the priority of ABOVETHIS."""
        self.tk.call(
            self._w, 'tag', 'raise', tagName, aboveThis)
    def tag_ranges(self, tagName):
        """Return a list of ranges of text which have tag TAGNAME."""
        return self.tk.splitlist(self.tk.call(
            self._w, 'tag', 'ranges', tagName))
    def tag_remove(self, tagName, index1, index2=None):
        """Remove tag TAGNAME from all characters between INDEX1 and INDEX2."""
        self.tk.call(
            self._w, 'tag', 'remove', tagName, index1, index2)
    def window_cget(self, index, option):
        """Return the value of OPTION of an embedded window at INDEX."""
        if option[:1] != '-':
            option = '-' + option
        if option[-1:] == '_':
            option = option[:-1]
        return self.tk.call(self._w, 'window', 'cget', index, option)
    def window_configure(self, index, cnf=None, **kw):
        """Configure an embedded window at INDEX."""
        return self._configure(('window', 'configure', index), cnf, kw)
    window_config = window_configure
    def window_create(self, index, cnf={}, **kw):
        """Create a window at INDEX."""
        self.tk.call(
            (self._w, 'window', 'create', index)
            + self._options(cnf, kw))
    def window_names(self):
        """Return all names of embedded windows in this widget."""
        return self.tk.splitlist(
            self.tk.call(self._w, 'window', 'names'))
    def yview_pickplace(self, *what):
        """Obsolete function, use see."""
        self.tk.call((self._w, 'yview', '-pickplace') + what)
