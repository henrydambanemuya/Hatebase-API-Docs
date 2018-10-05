# API v3.0

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

<table>
  <td><b>Filter</b></td>
  <td><b>Applicable query</b></td>
  <td><b>Format</b></td>
  <td><b>Useful for</b></td>
  </tr>
  <tr>
  <td>vocabulary</td>
  <td>vocabulary; sightings</td>
  <td>URL-encoded plaintext</td>
  <td>locating all sightings of a particular term</td>
  </tr>
  <tr>
  <td>variant_of</td>
  <td>vocabulary; sightings</td>
  <td>URL-encoded plaintext</td>
  <td>determining all variants of a particular term</td>
  </tr>
  <tr>
  <td>language</td>
  <td>vocabulary; sightings</td>
  <td>3-character ISO 639-3 code</td>
  <td></td>
  </tr>
  <tr>
  <td>about_ethnicity</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>about_nationality</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <td>about_religion</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>about_gender</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>about_sexual_orientation</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>about_disability</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>about_class</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>archaic</td>
  <td>vocabulary; sightings</td>
  <td>1 (for true) or 0 (for false)</td>
  <td></td>
  </tr>
  <tr>
  <td>page</td>
  <td>vocabulary; sightings</td>
  <td>any integer</td>
  <td>paginating through a large result</td>
  </tr>
  <tr>
  <td>country</td>
  <td>sightings</td>
  <td>2-character ISO 3166-2 code</td>
  <td></td>
  </tr>
  <tr>
  <td>city_or_community</td>
  <td>sightings</td>
  <td>URL-encoded plaintext</td>
  <td></td>
  </tr>
  <tr>
  <td>type</td>
  <td>sightings</td>
  <td>r (for recipient), o (for overheard), u (for used), t (for Twitter)</td>
  <td></td>
  </tr>
  <tr>
  <td>start_date</td>
  <td>sightings</td>
  <td>YYYY-mm-dd</td>
  <td>Defining the start of a date range</td>
  </tr>
  <tr>
  <td>end_date</td>
  <td>sightings</td>
  <td>YYYY-mm-dd</td>
  <td>Defining the end of a date range</td>
  </tr>
</table>

Some output parameters are not currently available as filters for obvious reasons, such as latitude and longitude (although in this case, a radial search may be made available in the future).

## Output Parameters

For illustrative purposes, output has been displayed below as XML.

```
[hatebase]
  [version]VARCHAR(6)[/status]
  [status]TEXT[/status]
  [page]TINYINT(3)[/page]
  [number_of_results]INT[/number_of_results]
  [number_of_results_on_this_page]INT[/number_of_results_on_this_page]
  [warnings]
    [warning_code]INT(4)[/warning_code]
    [human_readable_warning]VARCHAR(255)[/human_readable_warning]
  [/warnings]
  [errors]
    [error_code]INT(4)[/error_code]
    [human_readable_error]VARCHAR(255)[/human_readable_error]
  [/errors]
  [number_of_queries_today]INT[/number_of_queries_today]
  [data]

    {data structure is dependent on requested query type}

  [/data]
[/hatebase]```

Vocabulary data is presented with this structure:

```
    [datapoint]
        [vocabulary]VARCHAR(255)[/vocabulary]
        [variant_of]VARCHAR(255)[/variant_of]
        [pronunciation]VARCHAR(255)[/pronunciation]
        [meaning]TEXT[/meaning]
        [language]VARCHAR(3)[/language]
        [about_ethnicity]BINARY[/about_ethnicity]
        [about_nationality]BINARY[/about_nationality]
        [about_religion]BINARY[/about_religion]
        [about_gender]BINARY[/about_gender]
        [about_sexual_orientation]BINARY[/about_sexual_orientation]
        [about_disability]BINARY[/about_disability]
        [about_class]BINARY[/about_class]
        [archaic]BINARY[/archaic]
        [offensiveness]TINYINT(3)[/offensiveness]
        [number_of_revisions]INT[/number_of_revisions]
        [number_of_variants]INT[/number_of_variants]
        [variants]TEXT[/variants]
        [number_of_sightings]INT[/number_of_sightings]
        [last_sighting]DATETIME[/last_sighting]
        [number_of_citations]INT[/number_of_citations]
    [/datapoint]
```

Sightings data is presented with this structure:

```
    [datapoint]
        [sighting_id]INT(9)[/sighting_id]
        [date]DATE[/date]
        [country]VARCHAR(2)[/country]
        [city_or_community]VARCHAR(50)[/city_or_community]
        [lat]DECIMAL(11,7)[/lat]
        [long]DECIMAL(11,7)[/long]
        [type]CHAR(1)[/type]
        [human_readable_type]VARCHAR(15)[/human_readable_type]
        {plus related vocabulary data - see above}
    [/datapoint]
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

- Addition of human-readable warnings, error codes and sighting types
- Addition of offensiveness datapoint for vocabulary (will be empty until offensiveness meter is added to the website)
- Addition of pagination to all queries. This limits any query to 100 results, after which the results paginate, so to retrieve 150 results, you would query the API twice: page 1 would provide the first 100 results, and page 2 would provide the remaining 50 results.
- Addition of unique ID for sightings
