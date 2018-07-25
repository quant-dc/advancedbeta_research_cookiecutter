# {{cookiecutter.experiment_name}}

## Getting Started

### Prerequisites

## Description

{% if cookiecutter.description == "A Short Description of the project" %}
No description provided
{% else %}
{{cookiecutter.description}}
{% endif %}

## Hypothesis

{% if cookiecutter.hypothesis == "A Short Statement of the Hypotheses (; seperated for a list)" %}
No Hypothesis provided
{% else %}
{% set hypotheses = cookiecutter.hypothesis.split(';') %}
{% for item in hypotheses %}
* {{ item }}
{% endfor %}
{% endif %}

## Author

* **{{cookiecutter.author_name}}** *({{cookiecutter.author_email}})*

## Cookiecutter

*Made with advancedbeta_research_cookiecutter, __version: {{cookiecutter._version}}__*
