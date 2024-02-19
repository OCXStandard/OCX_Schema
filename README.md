![3DOCX.org logo](./docs/_static/logo.png)
# The Open Class 3D Exchange (OCX) Schema

## Introduction 
This is the official GitHub repository for the Open Class 3D Exchange (OCX) schema (working draft version) owned and managed by the [OCX Consortium](https://3Docx.org).  
The latest published version of the OCX schema is available from the consortium's website.

## Changelog
  * [CHANGELOG.md](CHANGELOG.md)

## Historic changes (pre 2.8.6)

  * [PRERELEASE_CHANGELOG.md](PRERELEASE_CHANGELOG.md)

## How to contribute
The schema file is maintained using an XML editor like Altova XMLSpy.
1. Installation: Simply download the schema files from the repository or clone it using git.
2. Create an [Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) for the proposed schema change. 
Follow [the recipe on the Wiki](https://github.com/OCXStandard/OCX_Schema/wiki) on how to register an issue.
3. Then create a branch from the issue, check out the branch and implement the proposed changes.
4. When the implementation is completed, create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
4. The pull request will have to be approved by the [OCXStandard maintainer](https://github.com/orgs/OCXStandard/teams/ocx-schema-team?query=role%3Amaintainer) before it can be included in the working draft.


## Schema versioning
The OCX schema is following the Python [PEP 440 versioning recommendations](https://peps.python.org/pep-0440/).

Following PEP 440, the canonical public version identifiers MUST comply with the following scheme:

``
  [N!]N(.N)*[{a|b|rc}N][.postN][.devN]
``
see the [PEP 440](https://peps.python.org/pep-0440/) for a detailed explanation.

## ``tbump`` versioning tool

The Python [``tbump``](https://pypi.org/project/tbump/) tool is used to automate and bump schema versions. tbump also provides the possibility for pre- and post-commit actions.
The project config file ``pyproject.toml`` contains the tbump settings.

### Usage

Assume that the current schema version is ``2.8.6``. To bump the schema version to the pre-release ``alpha`` version, the following command can be issued:

<pre><code>
> tbump 3.0.0-alpha
:: Bumping from 2.8.6 to 3.0.0-alpha
=> Would update current version in pyproject.toml
=> Would patch these files
- pyproject.toml:3 version = "2.8.6"
+ pyproject.toml:3 version = "3.0.0-alpha"
- pyproject.toml:34 current = "2.8.6"
+ pyproject.toml:34 current = "3.0.0-alpha"
- OCX_Schema.xsd:103 <xs:attribute name="schemaVersion" type="xs:string" use="required" fixed="2.8.6">
+ OCX_Schema.xsd:103 <xs:attribute name="schemaVersion" type="xs:string" use="required" fixed="3.0.0-alpha">
- OCX_Schema.xsd:12 xmlns:ocx="https://3docx.org/fileadmin//ocx_schema//V286//OCX_Schema.xsd"
+ OCX_Schema.xsd:12 xmlns:ocx="https://3docx.org/fileadmin//ocx_schema//V300alpha//OCX_Schema.xsd"
- OCX_Schema.xsd:14 targetNamespace="https://3docx.org/fileadmin//ocx_schema//V286//OCX_Schema.xsd"
+ OCX_Schema.xsd:14 targetNamespace="https://3docx.org/fileadmin//ocx_schema//V300alpha//OCX_Schema.xsd"
=> Would run these hooks before commit
* (1/4) $ python xsdata_package.py 3.0.0-alpha
* (2/4) $ xsdata generate OCX_Schema.xsd
* (3/4) $ gid add ./ocx_*
* (4/4) $ python insert_version.py 3.0.0-alpha
=> Would run these git commands
$ git add --update
$ git commit --message Bump to 3.0.0-alpha
$ git tag --annotate --message v3.0.0-alpha v3.0.0-alpha
$ git push --atomic origin working_draft v3.0.0-alpha
:: Looking good? (y/N)
>
</code></pre>




## Schema databinding 
See [DATABINDING.md](DATABINDING.md) 


## OCX Public License
The OCX standard is governed by the 3Docx.org (https://3Docx.org) Consortium Members and published under the
Apache 2.0 Public License conditions (the License).

You may obtain a copy of the License at:

[LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, the 3Docx standard and software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
The OCX Consortium is not liable to any use whatsoever of the distributed standard or software based on the standard.

See the License for the specific language governing permissions and limitations under the License.
