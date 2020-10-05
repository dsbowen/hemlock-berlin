<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style>##hemlock_berlin.**berlin**

<p class="func-header">
    <i>def</i> hemlock_berlin.<b>berlin</b>(<i>require=False</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-berlin/blob/master/hemlock_berlin/__init__.py#L9">[source]</a>
</p>

Add the Berlin Numeracy Test to a hemlock survey.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>require : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that responses are required.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>Question 1 : <i>hemlock.Page</i></b>
<p class="attr">
    The first page of the Berlin Numeracy Test.
</p></td>
</tr>
    </tbody>
</table>

####Notes

Although this function returns only the first page of the test, it is all
you need to add the full test to your survey. The submit function of the
page returned by this function adaptively generates additional pages of
the test.