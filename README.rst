A Minimum Python Template Project
==================================

.. image:: https://github.com/jackcizon/python_template/actions/workflows/ci.yaml/badge.svg
   :target: https://github.com/jackcizon/python_template/actions/workflows/ci.yaml
   :alt: CI


Delete the useless parts
------------------------

.. code-block:: bash

    cd python_template
    rm -rf .git
    rm docs/*.md
    rm -rf src/api/migrations  # must do this, otherwise `db init` operation will fail.
    cd ..
    mv python_template <your_project_name>
    cd docs
    mkdir _static  # if _static not exists
