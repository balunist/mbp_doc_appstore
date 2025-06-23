.. MapBoards Pro Documentation master file

.. toctree::
   :maxdepth: 2

Autodesk App Store Entry
^^^^^^^^^^^^^^^^^^^^^^^^

| Note: This is the Mac OS release of MapBoards Pro.  For the Windows release, click Win64 near the top of the page (under our logo, where it says OS).

| MapBoards Pro is a Autodesk Fusion 360 add-in designed to optimize the arrangement of 3D model parts onto material 
| boards for efficient manufacturing, particularly with laser cutters, CNC machines, and woodworking. It helps users 
| create flat layouts, generate cut lists, and export designs in formats like SVG and DXF. 

Key Features and Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Arrangement and Nesting**: 
|   MapBoards Pro automatically arranges the components of a 3D model onto one or more boards, optimizing material usage.
| **Material Optimization**: 
|   It helps determine the necessary material quantities and layout for a project, minimizing waste. 
| **Export Options**: 
|   The add-in can export the arranged layouts as SVG or DXF files, suitable for cutting with laser cutters or CNC machines. 
| **Cut Lists**: 
|   It can generate cut lists with accurate dimensions for each part, which can be used as a guide for manual cutting or as a checklist for material preparation. 
| **Customization**: 
|   MapBoards Pro offers various options for customizing the arrangement, including board dimensions, material types, and grain alignment. 
| **Reporting**: 
|   It can generate HTML reports with detailed information about the map, components, and material requirements. 
| **Integration with Fusion 360**: 
|   It seamlessly integrates into Fusion 360, allowing users to work directly within the design and manufacturing environment. 
  
Benefits
^^^^^^^^

| **Time Savings**:
|   Automates the process of arranging and nesting parts, saving significant time compared to manual methods. 
| **Material Savings**:
|   Optimizes material usage, reducing waste and cost. 
| **Improved Accuracy**:
|   Provides precise cut lists and layouts, minimizing errors in the manufacturing process. 
| **Enhanced Workflow**:
|   Streamlines the transition from design to manufacturing, making the process more efficient and user-friendly. 

| See detailed product description here `MapBoards Pro Description <https://balunist.github.io/mbp_docs/index.html#>`__
| See `App Store Installs <https://balunist.github.io/mbp_docs/usage/appstore.html>`__ for help with new or update installs. 

.. note:: MapBoards Pro can be launched using the toolbar icon or from the Create dropdown menu of the design workspace.

Replace note info with the following to match font size...

| MapBoards Pro can be launched using the toolbar icon or from the Create dropdown menu of the design workspace.

General Usage Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^

| Please follow the Getting Started link below which give you an overview of the available features.  It will be time well spent enabling 
| you to get the most out of this add-in.

| `Getting Started <https://balunist.github.io/mbp_docs/usage/quickstart.html>`__

| When a project moves from the design phase to the build phase, a material estimate and layout is needed to guide the manufacturing process. 
| MapBoards Pro can help with both. 

| With you model open in Fusion 360 Design workspace the following steps are taken:

| - Invoke MapBoards or MapBoard Pro
| - From the Lumber tab update the Width and Lengths for each board type (Material and Thickness) to match lumber dimensions available 
|   or that you plan to acquire 
| - Select the radial button on each board type to include them in the map generation
| - From the Options tab select the desired Map Output Type (Component Bodies), Arrangement Type, Component Spacing, Board Edge, Cut List and other 
|  options
| - Select OK to execute MapBoards Pro
 

| Once complete the created map will be displayed alongside the design on the XY plane (Z up) (optionally Y up on XZ plane). The map visibility 
| can be controlled with the LightBulb on the newly created map component. If the Cut List option is selected, a CSV file will be created at the 
| location specified. It will include a sorted list of all components with dimensions and a summary or required lumber. This file can be imported 
| into a spreadsheet such as Google Sheets. The Cut List can be used to create labels or be used as a checklist.  

| If you selected a Map Output Type of DXF file then the layered DXF file created can be imported into other CAD and CAM software for use with CNC, 
| water jet, plasma, or laser. The DXF file will have the selected profiles included as separate layers. 

| The DXF create can have 4 or more layers as perimeter, insets (one for each unique depth), cutouts, and labels. These layers are viewed from the 
| top view. Bottom insets can also optionally be included. The components are placed with the largest face down and the face with the most features
| facing up to be included with the export. A post-mapping task is available to flip components in the resulting map if needed.

| The same layered information is exported with the Export SVG context menu option. This SVG export can be used for further nesting when imported 
| other programs such as Deepest.  

| If you plan to complete the cutting with a CNC Router the following steps are suggested.

| To continue with Fusion's additive manufacturing you can right-click on the map object in the browser tree and select Manufacturing Model task, 
| select the board to export and the create setup option.  This will create a manufacturing model with the board isolated.  You can now create the 
| desired tool paths to drive your CNC or laser.   

| If you will be completing your manufacturing with other software or you machine setup requires DXF or SVG files to create tool paths that you can 
| use the post-mapping exports for SVG or DXF to export flat panel files for that purpose.

| Again, please go to the link below for a description of the available add-in features to help with this process.

| `MapBoards Pro Description <https://balunist.github.io/mbp_docs/index.html#>`__