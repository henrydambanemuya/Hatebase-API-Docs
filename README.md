<center><a href='https://hatebase.org'><img src="logo.png" width="200" ></a></center>

# How It Works

The Hatebase API accepts queries using a two-phase approach: the authentication handshake and then the actual query itself. In either scenario, the system is queried with a version number, an endpoint (which defines the type of information requested) and a payload containing input parameters (sent by POST), and then returns a resultset.

The URL structure for querying the API is as follows:

```
https://api.hatebase.org/1-0/authenticate
```

"1-0" represents the version number, and "authenticate" represents the endpoint. All versions and endpoints will be documented here.

# Authentication Phase

The API is queried with a key which is obtained from your Hatebase account:

```
{
  api_key: ABC123
}
```

The returned data provides the input parameters which were queried, plus a resultset (in this case a session token), plus any warnings and/or errors:


```
{
  datetime: gmt_time,
  key: ABC123,
  format: json,
  result: [
    token: DEF456,
    expires_on: "2018-01-01 12:00:00"
  ]
  errors: [
    [789, "Incorrect key"]
  ]
  warnings:[
    [012, "Unspecified format"]
  ]
}
```

Note that this result set is solely illustrative; a token would never be provided if there were errors, only warnings.

Tokens will expire within one hour of issue.

# Query Phase

The token provided in the authentication phase is used as an input parameter to authenticate phase two: the actual data query. The result set will look something like this:


```
{
  datetime: gmt_time,
  token: DEF456,
  expires_on: "2018-01-01 12:00:00",
  format: json,
  page: 1,
  total_pages: 14,
  result: [
  ]
  errors: [
  ]
  warnings:[
  ]
}
```

Again, this simple result set is solely illustrative; there is no need for empty key-value pairs.

# Daily Rate Limiting

Access to the API is limited by your plan's maximum daily query limit. It is strongly recommended that systems which connect with the API do not do so in user real-time. A safer architecture is to download data asynchronously and store locally for better real-time performance and no redundant data retrieval.

# Versions

<table>
  <tr>
  <td>[/v4.0/overview](v4-0/overview.md)</td>
  <td>Current</td>
  </tr>
  <tr>
  <td>[/v3.0/overview](v3-0/overview.md)</td>
  <td>Deprecated</td>
  </tr>
  <tr>
  <td>[/v2.0/overview](v2-0/overview.md)</td>
  <td>Deprecated</td>
  </tr>
  <tr>
  <td>/v1.0/overview</td>
  <td>Retired</td>
  </tr>
</table>

# Error Messages

<table>
  <tr>
  <td><b>Code</b></td>
  <td><b>Message</b></td>
  </tr>
  <tr>
  <td>0001</td>
  <td>Incorrect key</td>
  </tr>
  <tr>
  <td>0002</td>
  <td>Incorrect token</td>
  </tr>
  <tr>
  <td>0003</td>
  <td>Expired token; please reauthenticate using your API key</td>
  </tr>
  <tr>
  <td>0004</td>
  <td>The version of the API is now retired; please update your queries to resume accessing the API.</td>
  </tr>
  <tr>
  <td>0005</td>
  <td>Daily query cap exceeded; please review documentation on connecting asynchronously to avoid exceeding limits.</td>
  </tr>
</table>

# Warning Messages

<table>
  <tr>
  <td><b>Code</b></td>
  <td><b>Message</b></td>
  </tr>
  <tr>
  <td>0001</td>
  <td>API version deprecated and approaching retirement; please upgrade to the latest version</td>
  </tr>
  <tr>
  <td>0002</td>
  <td>Daily query cap imminent; please review documentation on connecting asynchronously to avoid exceeding limits.</td>
  </tr>
  <tr>
  <td>0003</td>
  <td>No output format specified, so defaulted to JSON</td>
  </tr>
  <tr>
  <td>0004</td>
  <td>No page number specified, so defaulted to 1</td>
  </tr>
  <tr>
  <td>0005</td>
  <td>Invalid input parameter received</td>
  </tr>
</table>

# Please Contact Us

Although every effort has been made to ensure that this documentation accurately reflects the operation of the API, please advise us if you discover any discrepancies.
