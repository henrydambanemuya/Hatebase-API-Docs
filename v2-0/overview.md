# API v2.0

## Input Parameters

The high-level schema for the Hatebase API is as follows:

~~~
http://api.hatebase.org/version/key/query-type/output/encoded-filters
~~~

<table>
  <tr>
  <td><b>URL Segment</b></td>
  <td><b>Format</b></td>
  <td><b>Options</b></td>
  </tr>
  <tr>
  <td>version</td>
  <td>v{increment}-{sub-increment}</td>
  <td></td>
  </tr>
  <tr>
  <td>key</td>
  <td>{32-digit key}</td>
  <td></td>
  </tr>
  <tr>
  <td>query type</td>
  <td>{query type}</td>
  <td>vocabulary; sightings</td>
  </tr>
  <tr>
  <td>output</td>
  <td>{output}</td>
  <td>xml; json</td>
  </tr>
  <tr>
  <td>(encoded) filters</td>
  <td>{key}%3D{value}%7C{key}%3D{value}</td>
  <td></td>
  </tr>
</table>

Filters are key/value pairs which correspond to output parameters. So for instance, to retrieve all sightings of English-language vocabulary pertaining to religion, the filter segment would properly read **language%3Deng%7Cabout_religion%3D1**.

The following additional filters are also available:

<table>
  <tr>
  <td><b>Query type</b></td>
  <td><b>Filter</b></td>
  <td><b>Format</b></td>
  <td><b>Useful for</b></td>
  </tr>
  <tr>
  <td>Sightings</td>
  <td>start_date</td>
  <td>YYYY-mm-dd</td>
  <td>Defining the start of a date range</td>
  </tr>
  <tr>
  <td></td>
  <td>end_date</td>
  <td>YYYY-mm-dd</td>
  <td>Defining the end of a date range</td>
  </tr>
</table>

Some output parameters are not currently available as filters for obvious reasons, such as latitude and longitude (although in this case, a radial search may be made available in the future).

## Output Parameters

For illustrative purposes, output has been displayed below as XML.

```
<hatebase>
  <version>VARCHAR(6)</status>
  <status>TEXT</status>
  <warnings>
    <warning_code>INT(4)</warning_code>
  </warnings>
  <errors>
    <error_code>INT(4)</error_code>
  </errors>
  <number_of_queries_today>INT</number_of_queries_today>
  <data>

    {data structure is dependent on requested query type}

  </data>
</hatebase>
```

Vocabulary data is presented with this structure:

```
<datapoint>
    <vocabulary>VARCHAR(255)</vocabulary>
    <variant_of>VARCHAR(255)</variant_of>
    <pronunciation>VARCHAR(255)</pronunciation>
    <meaning>TEXT</meaning>
    <language>VARCHAR(3)</language>
    <about_ethnicity>BINARY</about_ethnicity>
    <about_nationality>BINARY</about_nationality>
    <about_religion>BINARY</about_religion>
    <about_gender>BINARY</about_gender>
    <about_sexual_orientation>BINARY</about_sexual_orientation>
    <about_disability>BINARY</about_disability>
    <about_class>BINARY</about_class>
    <archaic>BINARY</archaic>
    <number_of_revisions>INT</number_of_revisions>
    <number_of_variants>INT</number_of_variants>
    <variants>TEXT</variants>
    <number_of_sightings>INT</number_of_sightings>
    <last_sighting>DATETIME</last_sighting>
    <number_of_citations>INT</number_of_citations>
</datapoint>
```

Sightings data is presented with this structure:

```
<datapoint>
    <date>DATE</date>
    <country>VARCHAR(2)</country>
    <city_or_community>VARCHAR(50)</city_or_community>
    <lat>DECIMAL(11,7)</lat>
    <long>DECIMAL(11,7)</long>
    <type>CHAR(1)</type>
    {plus related vocabulary data - see above}
</datapoint>
```

## Error Handling

Incorrectly configured input parameters will result in an error being returned with the data. If the proper output format parameter cannot be determined, the default output for error messages is XML.

### Warning codes

<table>
  <tr>
  <td>1</td>
  <td>Approaching maximum daily queries.</td>
  </tr>
  <tr>
  <td>2</td>
  <td>No vocabulary was retrieved based on your input parameters.</td>
  </tr>
  <tr>
  <td>3</td>
  <td>No sightings were retrieved based on your input parameters.</td>
  </tr>
  <tr>
  <td>4</td>
  <td>This API version has been deprecated and will soon be retired. Please upgrade to the latest API.</td>
  </tr>
</table>

### Error codes

<table>
  <tr>
  <td>1</td>
  <td>No valid filters found.</td>
  </tr>
  <tr>
  <td>2</td>
  <td>Missing API key.</td>
  </tr>
  <tr>
  <td>3</td>
  <td>Invalid API key.</td>
  </tr>
  <tr>
  <td>4</td>
  <td>Maximum daily queries already reached; the query limit resets every 24 hours.</td>
  </tr>
  <tr>
  <td>5</td>
  <td>Unable to determine a valid query type.</td>
  </tr>
  <tr>
  <td>6</td>
  <td>This API version is now retired. Please upgrade to the latest API.</td>
  </tr>
</table>

## Changelog

- In the sightings query, recipient_or_overheard has been changed to type to accommodate a third potential value. So this field will now return "r" (recipient), "o" (overheard) or "u" (used).
- A version field has been added.
- Structured warning codes and error codes have been added.
