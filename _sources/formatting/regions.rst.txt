.. _regions:

Source code regions
===================

Use special markers to specify regions in big source code files / classes::

    class MyClass:

        # region plots

        def scatter_plot(self):
            pass

        def line_plot(self):
            pass

        # endregion

        # region io

        @staticmethod
        def load(path):
            pass

        def save(self, path):
            pass

        # endregion
        

Then use the following extension:

- [Region Viewer](https://marketplace.visualstudio.com/items?itemName=SantaCodes.santacodes-region-viewer)

to navigate the regions in an "Explorer" pane.
