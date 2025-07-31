.. MapBoards Pro Documentation master file

.. toctree::
   :maxdepth: 2

Autodesk App Store Entry
^^^^^^^^^^^^^^^^^^^^^^^^

.. role:: blue-bold

| Note: This is the Mac OS release of MapBoards Pro.  For the Windows release, click Win64 near the top of the page (under our logo, where it says OS).

| MapBoards Pro is a Autodesk Fusion 360 add-in designed to optimize the arrangement of 3D components onto material
| boards for efficient manufacturing, particularly with laser cutters, CNC machines, and woodworking. It helps users
| create flat layouts, generate cut lists, and export designs as either SVG or DXF files.

Key Features and Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Arrangement and Nesting**:
|   MapBoards Pro (MBP) automatically arranges copies of components in a 3D model onto one or more boards, optimizing material usage.
| **Material Optimization**:
|   MBP helps determine the necessary material quantities and layout for a project, minimizing waste.
| **Export Options**:
|   MBP can export the arranged layouts as SVG or DXF files, suitable for cutting with laser cutters or CNC machines.
| **Cut Lists**:
|   MBP can generate cut lists with accurate dimensions for each component, which can be used as a guide for manual cutting or as a checklist for material preparation.
| **Customization**:
|   MBP offers various options for customizing the arrangement, including board dimensions, material types, and grain alignment.
| **Reporting**:
|   MBP can generate HTML reports with detailed information about the map, its components, and material requirements.
| **Integration with Fusion 360**:
|   MBP seamlessly integrates into Fusion 360, allowing users to work directly within the design and manufacturing environment.

Benefits
^^^^^^^^

| **Time Savings**:
|   Automates the process of arranging components, saving significant time compared to manual methods.
| **Material Savings**:
|   Optimizes material usage, reducing waste and cost.
| **Improved Accuracy**:
|   Provides cut lists of components and required materials with precise dimensions minimizing errors in the manufacturing process.
| **Enhanced Workflow**:
|   Analyzes the components in a model and produces a map of component copies on the required material. The created map can then be exported 
|   to either a Fusion manufacturing model or an external SVG or DXF file. This streamlines the transition from design to manufacturing,
|   making the process more efficient and user-friendly.

| See detailed product description here `MapBoards Pro Description <https://balunist.github.io/mbp_docs/index.html#>`__
| See `App Store Installs <https://balunist.github.io/mbp_docs/usage/appstore.html>`__ for help with new or update installs.

.. note::

   :MapBoards Pro can be launched using the toolbar icon or from the Create dropdown menu of the design workspace.:

General Usage Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^

See `The Basics <https://balunist.github.io/mbp_docs2/the_basics/index.html>`__ for an introduction to MapBoards Pro 
and an overview of the available features. Reading this user guide before getting started, will help you get the most 
out of MapBoards Pro.

| When a project moves from the design phase to the build phase, a material estimate and layout is needed to guide the manufacturing process.
| MapBoards Pro can help with both.

| Begin with your 3D model open in the Fusion 360 Design Workspace:

| - Invoke MapBoard Pro
| - From the Lumber tab, update the Width and Length for each board type to match lumber dimensions available
|   or that you plan to acquire
| - Select the radial button on the left side of each board type to include them in the map generation
| - Use the options tab to select your desired Map Output Type, Arrangement Type, Component Spacing, Board Edge, Cut List and other
| - Select OK to run MapBoards Pro to create map using copies of the components in the model

| Once complete, the created map will be displayed alongside the design on the XY plane (Z up) (optionally Y up on XZ plane). The map visibility
| can be controlled with the visibility icon (LightBulb) on the newly created map component. Selecting the Cut List option will create a file which can 
| be used for label making or a checklist.

| MBP can also export maps as layered DXF files, which can be imported into other CAD and CAM software for use with CNC,
| water jet, plasma, or laser. The DXF file will include selected profiles as separate layers.

| DXF files created can have 4 or more layers as perimeters, insets (one for each unique depth), cutouts, and labels. These layers are displayed in the
| top view. Bottom insets can also optionally be included. The components are placed with the largest face down and the face with the most features
| facing up to be included with the export. A post-mapping task is available to flip components in the resulting map if needed.

| The same layered information is exported with the SVG files. This SVG files can be used for further nesting when imported
| into other programs such as Deepest.

| If you plan to complete cutting with a CNC router, the following steps are suggested:

| Continue with Fusion's additive manufacturing by right-clicking on the map object in the browser tree and selecting Manufacturing Model.
| This will create a manufacturing model with the board isolated. You can now create the desired tool paths to drive your CNC or laser.

| If you will be completing your manufacturing with other software or your machine setup requires DXF or SVG files to create tool paths, use the 
| post-mapping export tasks to create SVG or DXF files for that purpose.

| For a description of the available add-in features, visit the link below.

| `MapBoards Pro Description <https://balunist.github.io/mbp_docs/index.html#>`__

