
Bamboo Boy is a way to share setup and teardown logic between tests,
deployments, and development environments. It can reduce boilerplate
logic in test methods, eliminate the need for fixtures or traditional
scaffolding, and promote separation of logic between test state and
assertions.

The "Boy" is a reference to utilizing factory\_boy and extending its
basic philosophy.

The "Bamboo" is the basis of the implementation metaphor:

-  A "Clump" is a collection of objects and setup / teardown logic.
-  A "canopy" is built by running the "build\_canopy" method of a Clump.
-  The canopy is used to access the objects. A function is said to be
   running "with a canopy" if it uses the @with\_canopy decorator.

Maybe you already have the following Thing and its Factory.
-----------------------------------------------------------

.. code:: python

    import factory
    
    
    class Thing(object):
        def do_your_thing(self):
            return True
    
        
    class ThingFactory(factory.Factory):
        class Meta:
            model = Thing
Now, you can create a "Clump" of reusable logic.
------------------------------------------------

.. code:: python

    from bamboo_boy.materials import Clump
    
    
    class ThingExists(Clump):
        '''
        Ensures that three Thing objects exist.
        '''
        def build_canopy(self):
            self.include_factory(ThingFactory, 3)  # We can also include *args and **kwargs here; they'll be passed on to the factory
Then, in a test:
----------------

.. code:: python

    import unittest
    from bamboo_boy.utils import with_canopy
    
    
    @with_canopy(ThingExists)
    class TestThings(unittest.TestCase):
    
        def test_that_thing_does_its_thing(self):
            lists_of_things = self.canopy.objects[ThingFactory]
            first_list_of_things = lists_of_things[0]
            first_thing = first_list_of_things[0]
            self.assertTrue(first_thing.do_your_thing())
.. code:: python

    %load_ext ipython_nose

.. parsed-literal::

    The ipython_nose extension is already loaded. To reload it, use:
      %reload_ext ipython_nose


.. code:: python

    %nose


.. raw:: html

    <div id="ipython_nose_cbdf26a98ed94655b2571e327eb28d00"></div>




.. parsed-literal::

    DEBUG:factory.generate:BaseFactory: Preparing __main__.ThingFactory(extra={})
    DEBUG:factory.generate:<class '__main__.ThingFactory'>: Setting up next sequence (0)
    DEBUG:factory.containers:LazyStub: Computing values for __main__.ThingFactory()
    DEBUG:factory.containers:LazyStub: Computed values, got __main__.ThingFactory()
    DEBUG:factory.generate:BaseFactory: Generating __main__.ThingFactory()
    DEBUG:factory.generate:BaseFactory: Preparing __main__.ThingFactory(extra={})
    DEBUG:factory.containers:LazyStub: Computing values for __main__.ThingFactory()
    DEBUG:factory.containers:LazyStub: Computed values, got __main__.ThingFactory()
    DEBUG:factory.generate:BaseFactory: Generating __main__.ThingFactory()
    DEBUG:factory.generate:BaseFactory: Preparing __main__.ThingFactory(extra={})
    DEBUG:factory.containers:LazyStub: Computing values for __main__.ThingFactory()
    DEBUG:factory.containers:LazyStub: Computed values, got __main__.ThingFactory()
    DEBUG:factory.generate:BaseFactory: Generating __main__.ThingFactory()








.. raw:: html

        <style type="text/css">
            span.nosefailedfunc {
                font-family: monospace;
                font-weight: bold;
            }
            div.noseresults {
                width: 100%;
            }
            div.nosebar {
                float: left;
                padding: 1ex 0px 1ex 0px;
            }
            div.nosebar.fail {
                background: #ff3019; /* Old browsers */
                /* FF3.6+ */
                background: -moz-linear-gradient(top, #ff3019 0%, #cf0404 100%);
                /* Chrome,Safari4+ */
                background: -webkit-gradient(linear, left top, left bottom,
                                             color-stop(0%,#ff3019),
                                             color-stop(100%,#cf0404));
                /* Chrome10+,Safari5.1+ */
                background: -webkit-linear-gradient(top, #ff3019 0%,#cf0404 100%);
                /* Opera 11.10+ */
                background: -o-linear-gradient(top, #ff3019 0%,#cf0404 100%);
                /* IE10+ */
                background: -ms-linear-gradient(top, #ff3019 0%,#cf0404 100%);
                /* W3C */
                background: linear-gradient(to bottom, #ff3019 0%,#cf0404 100%);
            }
            div.nosebar.pass {
                background: #52b152;
                background: -moz-linear-gradient(top, #52b152 1%, #008a00 100%);
                background: -webkit-gradient(linear, left top, left bottom,
                                             color-stop(1%,#52b152),
                                             color-stop(100%,#008a00));
                background: -webkit-linear-gradient(top, #52b152 1%,#008a00 100%);
                background: -o-linear-gradient(top, #52b152 1%,#008a00 100%);
                background: -ms-linear-gradient(top, #52b152 1%,#008a00 100%);
                background: linear-gradient(to bottom, #52b152 1%,#008a00 100%);
            }
            div.nosebar.skip {
                background: #f1e767;
                background: -moz-linear-gradient(top, #f1e767 0%, #feb645 100%);
                background: -webkit-gradient(linear, left top, left bottom,
                                             color-stop(0%,#f1e767),
                                             color-stop(100%,#feb645));
                background: -webkit-linear-gradient(top, #f1e767 0%,#feb645 100%);
                background: -o-linear-gradient(top, #f1e767 0%,#feb645 100%);
                background: -ms-linear-gradient(top, #f1e767 0%,#feb645 100%);
                background: linear-gradient(to bottom, #f1e767 0%,#feb645 100%);
            }
            div.nosebar.leftmost {
                border-radius: 4px 0 0 4px;
            }
            div.nosebar.rightmost {
                border-radius: 0 4px 4px 0;
            }
            div.nosefailbanner {
                border-radius: 4px 0 0 4px;
                border-left: 10px solid #cf0404;
                padding: 0.5ex 0em 0.5ex 1em;
                margin-top: 1ex;
                margin-bottom: 0px;
            }
            div.nosefailbanner.expanded {
                border-radius: 4px 4px 0 0;
                border-top: 10px solid #cf0404;
            }
            pre.nosetraceback {
                border-radius: 0 4px 4px 4px;
                border-left: 10px solid #cf0404;
                padding: 1em;
                margin-left: 0px;
                margin-top: 0px;
                display: none;
            }
        </style>
        
        <script>
            setTimeout(function () {
                $('.nosefailtoggle').bind(
                    'click',
                    function () {
                        $(
                            $(this)
                                .parent().toggleClass('expanded')
                                .parent()
                                .children()
                                .filter('.nosetraceback')
                        ).toggle();
                    }
                );},
                0);
        </script>
        
        <div class="noseresults">
          <div class="nosebar fail leftmost" style="width: 0%">
              &nbsp;
          </div>
          <div class="nosebar skip" style="width: 0%">
              &nbsp;
          </div>
          <div class="nosebar pass rightmost" style="width: 100%">
              &nbsp;
          </div>
          1/1 tests passed
        </div>
        

