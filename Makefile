# A self-documenting Makefile
# You can set these variables from the command line, and also
# from the environment for the first two.
SOURCE = ./ocx
CONDA_ENV = ocx_schema
# PS replacements for sh
RM = 'del -Confirmed False'

PACKAGE := ocx
MODULES := $(wildcard $(PACKAGE)/*.py)

# CONDA TASKS ##################################################################
# PROJECT setup using conda and powershell
.PHONY: conda-create
conda-create:  ## Create a new conda environment with the python version and basic development tools
	@conda env create -f environment.yml
	@conda activate $(CONDA_ENV)
cc: conda-create
.PHONY: cc

conda-upd:   ## Update the conda development environment when environment.yaml has changed
	@conda env update -f environment.yml

cu: conda-upd
.PHONY:cu

conda-activate: ## Activate the conda environment for the project
	@conda activate $(CONDA_ENV)
ca: conda-activate
.PHONY: ca

conda-clean: ## Purge all conda tarballs, log files and caches
	conda clean -a -y
.Phony: conda-clean


# PROJECT DEPENDENCIES ########################################################

# VIRTUAL_ENV ?= ${VENV}
# DEPENDENCIES := $(VIRTUAL_ENV)/$(shell cksum pyproject.toml)


# Color output
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# DOCUMENTATION ##############################################################
SPHINXBUILD = sphinx-build -E -b html docs dist/docs

doc-serve: ## Open the the html docs built by Sphinx
	@cmd /c start "dist/html/index.html"

ds: doc-serve
.PHONY: ds

doc-help:  ## Sphinx options when running make from the docs folder
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

doc: ## Build the html docs using Sphinx. For other Sphinx options, run make in the docs folder
	@$(SPHINXBUILD)  -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD)  "$(SOURCEDIR)" "$(BUILDDIR)/$(SPHINXOPTS)" -b "$(SPHINXOPTS)"



# RUN ##################################################################

# GENERATE DATABINDINGS ########################################################

generate: ## Generate the python data-bindings. See the .xsdata.xml file for xsdata settings
	@xsdata generate OCX_ext_rudder.xsd

# HELP ########################################################################


.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

#-----------------------------------------------------------------------------------------------



