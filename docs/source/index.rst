====================
EXMOTO Documentation
====================

EXMOTO (**Ex**\ perimental **Mo**\ deling **To**\ olkit) is a toolkit used to support trajectory perturbation, database management, and centralized variable management for large-scale (large number of variables, multi-sectoral, etc.) modeling.
- Uncertainty specification and trajectory sampling mechanism
- A data pipeline management system
- Scalable architecture
- Customizable variable setup through sector-level categorization


Check out the `General Data <../general_data.htm>`_ section to get started.



EXMOTO and Documentation Terminology 
---------------------------------------


Subsectors
^^^^^^^^^^
- Subsectors are groupings 

Categories
^^^^^^^^^^
**Categories** are associated with subsectors and represent multiple instantiations of the same conceptual ModelVariable. For example, in `https://sisepuede.readthedocs.io/en/latest/`, the Transportation subsector is used to calculate emissions from the combustion of fuels to achieve transportation. This subsector is associated with different categories (or types) of transport, i.e.,  `aviation`, `human_powered`, `powered_bikes`, `public`, `rail_freight`, `rail_passenger`, `road_heavy_freight`, `road_heavy_regional`, `road_light`, and `water_borne`.  Categories can be used within one or more subsectors--that are used to 

Variables and Fields
^^^^^^^^^^^^^^^^^^^^
The SISEPUEDE integrated modeling framework makes use of a generalizable variable schematic to define input variables for models. There are two components to this naming system:

#. **Model Variables** These are conceptual variables--for example, `Crop Yield Factor`--that are used to group

#. **Variable Fields** These are direct inputs to the SISEPUEDE models, entered as fields in a data frame. For example, the input variables associated with `Crop Yield Factor` include...

- variables are abstract groupings of variables for a defined category
   - some variables represent no categories
   - some represent all
   - some represent only a few
- the model fundamentally reads in data frames with fields; those fields are defined by the variable construct
- reading the variable definition tables
   - Variable Name
   - Variable Schema
   - Categories
   - Simplex Group (probability simplex)
.. note::
   SIMPLEX NOTE EXAMPLE Note that the sum of all initial fractions of area across land use categories *u* should be should equal 1 to , i.e. :math:`\sum_u \varphi_u = 1`, where :math:`\varphi_{\text{$CAT-LANDUSE$}} \to` ``frac_lu_$CAT-LANDUSE$`` at period *t*.

   - Default value
   - Other attributes



Metavariables and Constructing Input Parameters
-----------------------------------------------


-


 



Contents
--------
.. toc example struct from https://github.com/readthedocs/sphinx_rtd_theme/blob/c9b1bde560d8ee31400e4e4f92f2e8d7a42265ce/docs/index.rst
.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html

.. toctree::
   :caption: Getting Started
   :hidden:

   installation
   quick_start
   sisepuede_concept
   analytical_parameters

.. toctree::
   :caption: Variables, Categories, and Data
   :hidden:

   general_data
   afolu
   circular_economy
   energy_consumption
   energy_production
   ippu
   socioeconomic

.. toctree::
   :caption: Defining Strategies
   :hidden:

   strategies
   transformations
   transformers 

.. toctree::
   :caption: Managing Experiments
   :hidden:

   dimensions_of_analysis
   entering_data
   running_models
   sisepuede_database

.. toctree::
   :caption: Mathematical Specifications
   :hidden:

   mathdoc_afolu
   mathdoc_circular_economy
   mathdoc_economic_impact
   mathdoc_energy
   mathdoc_ippu

.. toctree::
   :caption: Community
   :hidden:

   contribute
