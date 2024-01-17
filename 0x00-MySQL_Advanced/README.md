MySQL advanced

pull and run mysql on docker with root user & password
`docker run --name=my-image-name -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql`
access the container
`docker exec -it my-name bin/bash`

Access MySQL
`mysql`

create user

```CREATE USER 'user'@'localhost';
	GRANT ALL PRIVILEGES ON base.* TO 'user'@'localhost' IDENTIFIED BY 'password';
	GRANT SELECT, INSERT, DELETE ON base.* TO 'user'@'localhost' IDENTIFIED BY 'password';
	FLUSH PRIVILEGES;
```

run query on mysql db on docker from localhost:
`mysql -h localhost -P 3306 --protocol=tcp -u root -p hbtn_0d_tvshows`

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">

      <script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({"userId":343517,"visitorType":"student","batch":{"id":80,"fullNameWithC":"NBO-0223 (C#13)","schoolLocation":{"id":7,"name":"Nairobi"}},"curriculum":{"id":17,"name":"Short Specializations"}});

    window.gtm_user_custom_event = function (name, options) {
      if (typeof name === 'undefined') {
        return;
      }

      window.dataLayer.push({
        customEventOptions: typeof options !== 'undefined' ? options : {},
        event: name,
      });
    }

  </script>

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-N4C8MF2');</script>
  <!-- End Google Tag Manager -->

    <title>Project: 0x00. MySQL advanced | Nairobi Intranet</title>

      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" media="all" href="/assets/application_alx-8941610700856adf24a6e389e4f744b0cefa6db7b3bc8157ea63b16ddcf11590.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <script src="/assets/application-e108fb75f939d72d47f0e99c7163aee8c5572427c1e62e5b50334df42d03f2d3.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon_alx.ico" />
      <meta name="csrf-param" content="authenticity_token" />

<meta name="csrf-token" content="0JPK4JFC6Yf7GVOj3a3OdninSnspX_Z8Uui6y8whfEruWaBoiutD17ibX81ZwfBFHyHtI-SBjrTiTZsmPXdNAg" />

      <link rel="apple-touch-icon" href="/apple-touch-icon_alx.png">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->

      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>

      <!-- intro.js for interactive onboarding -->

      <!-- React -->
      <script src="/packs/js/application-cee6709d99758d08c595.js"></script>
      <link rel="stylesheet" media="screen" href="/packs/css/application-87456da7.css" />

  </head>

  <body class="signed_in env_production notranslate"
        translate="no"
        class="notranslate"
        data-theme-suffix="_alx">
      <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N4C8MF2"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

      <input type="hidden" id="hbtn-slack-url" value="https://alx-students.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">

  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>

</a> </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My Planning"><a href="/planning/me"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar "></i></div><div class="visible-xs">My Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa-solid fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa-solid fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">


      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa-solid fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>

<hr class="visible-xs">

<li>

      <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Discord">
        <a rel="noreferrer" target="_blank" href="https://discord.com/app">
          <div class="icon discord">
            <i aria-hidden="true" class="fa-brands fa-discord "></i>
          </div>
          <div class="visible-xs">Discord</div>

</a> </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.amazonaws.com/alx-intranet.hbtn.io/users/photos/000/343/517/thumb/profile.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240117%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240117T215431Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=67cf70c2e7c20c66d128b1b085767dbb8bab09e046ddb56e0e8a64c83e24d251')"></div>
        </div>

      <div class="visible-xs">My Profile</div>

</a> </div>

</li>

    </ul>

  </div>
</nav>

      <div class="hidden-xs navigation sidebar">

  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My Planning"><a href="/planning/me"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar "></i></div><div class="visible-xs">My Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa-solid fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa-solid fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">


      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa-solid fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>

<hr class="visible-xs">

<li>

      <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Discord">
        <a rel="noreferrer" target="_blank" href="https://discord.com/app">
          <div class="icon discord">
            <i aria-hidden="true" class="fa-brands fa-discord "></i>
          </div>
          <div class="visible-xs">Discord</div>

</a> </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.amazonaws.com/alx-intranet.hbtn.io/users/photos/000/343/517/thumb/profile.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240117%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240117T215431Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=67cf70c2e7c20c66d128b1b085767dbb8bab09e046ddb56e0e8a64c83e24d251')"></div>
        </div>

      <div class="visible-xs">My Profile</div>

</a> </div>

</li>

  </ul>
</div>

    <main>
        <div id="layout-bars">

          <div class="px-5 py-3" id="student-switch-curriculum">

  <div class="dropdown d-flex flex-column gap-1">
    <span class="fs-small text-muted">Curriculum</span>

    <div aria-haspopup="true" aria-expanded="false" class="align-items-center d-flex gap-3" data-toggle="dropdown" id="student-switch-curriculum-dropdown" role="button">
      <div class="d-flex flex-column" style="line-height: 16px">
        <span class="fs-4 fw-600">
          Short Specializations
        </span>
        <span class="fs-small text-muted">
          Average: <span class="fw-500">150.0%</span>
        </span>
      </div>

      <div class="d-flex flex-column justify-content-center">
        <span style="margin-bottom: -4px">
          <i aria-hidden="true" class="fa-solid fa-angle-up  fa-fw"></i>
        </span>
        <span style="margin-top: -4px">
          <i aria-hidden="true" class="fa-solid fa-angle-down  fa-fw"></i>
        </span>
      </div>
    </div>

    <ul aria-labelledby="student-switch-curriculum-dropdown" class="dropdown-menu fs-5">
        <li>
          <a href="/curriculums/1/observe">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                  SE Foundations
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">163.05%</span>
                </span>
              </div>

            </div>

</a> </li>
<li>
<a href="/curriculums/17/observe">
<div class="align-items-center d-flex py-2">
<div class="d-flex flex-column" style="line-height: 16px">
<span class="fs-4 fw-500">
Short Specializations
</span>
<span class="text-muted">
Average: <span class="fw-500">150.0%</span>
</span>
</div>

                <span class="fw-600 text-info" style="margin-left: 42px">
                  <i aria-hidden="true" class="fa-solid fa-check "></i>
                </span>
            </div>

</a> </li>
</ul>

  </div>
</div>

        </div>

      <article class="">
          <div class="alert alert-info sm-gap big-zindex">
              You just released the advanced tasks of this project. Have fun!
          </div>



<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x00. MySQL advanced</h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:35,&quot;value&quot;:&quot;Back-end&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:37,&quot;value&quot;:&quot;SQL&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:38,&quot;value&quot;:&quot;MySQL&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;author&quot;:&quot;Guillaume Plessis, Senior Cloud \u0026 System Engineer at WeWork and Guillaume, CTO at Holberton school&quot;,&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:true,&quot;auto_correction_available_at&quot;:&quot;2024-01-17T18:00:00.000+03:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2024-01-17T06:00:00.000+03:00&quot;,&quot;ends_at&quot;:&quot;2024-01-19T06:00:00.000+03:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-01-21T06:00:00.000+03:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"></div>

    <div id="project_id" style="display: none" data-project-id="1232"></div>





        <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Concepts</h3>
    </div>
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at this concept:</em>
      </p>

      <ul>
          <li>
            <a href="/concepts/555">Advanced SQL</a>
          </li>
      </ul>
    </div>

  </div>

      <div class="panel panel-default" id="project-description">

  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/8w9di_hk19DIMSBEV3EayQ" title="MySQL cheatsheet" target="_blank">MySQL cheatsheet</a></li>
<li><a href="/rltoken/2GJbZ48zRPA70o2YhTdH7g" title="MySQL Performance: How To Leverage MySQL Database Indexing" target="_blank">MySQL Performance: How To Leverage MySQL Database Indexing</a></li>
<li><a href="/rltoken/K180X2OCzb6gzPngjn-EIg" title="Stored Procedure" target="_blank">Stored Procedure</a></li>
<li><a href="/rltoken/cJ1qA4o-rRm4rWIsqYKSZg" title="Triggers" target="_blank">Triggers</a></li>
<li><a href="/rltoken/vHg1z3UAOcWMvOt8xZHeiA" title="Views" target="_blank">Views</a></li>
<li><a href="/rltoken/g-c1m6iljScpi4LeqxBRqQ" title="Functions and Operators" target="_blank">Functions and Operators</a></li>
<li><a href="/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ" title="Trigger Syntax and Examples" target="_blank">Trigger Syntax and Examples</a></li>
<li><a href="/rltoken/X789nJ22H6HVh1uCQPl0lg" title="CREATE TABLE Statement" target="_blank">CREATE TABLE Statement</a></li>
<li><a href="/rltoken/mfrWMt1KL3NHXblJykMgZg" title="CREATE PROCEDURE and CREATE FUNCTION Statements" target="_blank">CREATE PROCEDURE and CREATE FUNCTION Statements</a></li>
<li><a href="/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ" title="CREATE INDEX Statement" target="_blank">CREATE INDEX Statement</a></li>
<li><a href="/rltoken/FEZNlZFKZmD1ISnLINkCwQ" title="CREATE VIEW Statement" target="_blank">CREATE VIEW Statement</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/NEA0Fr7muHfukl5lziVAhg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create tables with constraints</li>
<li>How to optimize queries by adding indexes</li>
<li>What is and how to implement stored procedures and functions in MySQL</li>
<li>What is and how to implement views in MySQL</li>
<li>What is and how to implement triggers in MySQL</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be executed on Ubuntu 18.04 LTS using <code>MySQL 5.7</code> (version 5.7.30)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Use &ldquo;container-on-demand&rdquo; to run MySQL</h3>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - Python 3.7</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h3>How to import a SQL dump</h3>

<pre><code>$ echo &quot;CREATE DATABASE hbtn_0d_tvshows;&quot; | mysql -uroot -p
Enter password: 
$ curl &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql&quot; -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo &quot;SELECT * FROM tv_genres&quot; | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

  </div>
</div>

          <h2 class="gap">Tasks</h2>

    <div data-role="task11633" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11633">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. We are all unique!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a table <code>users</code> following these requirements:</p>

<ul>
<li>With these attributes:

<ul>
<li><code>id</code>, integer, never null, auto increment and primary key</li>
<li><code>email</code>, string (255 characters), never null and unique</li>
<li><code>name</code>, string (255 characters)</li>
</ul></li>
<li>If the table already exists, your script should not fail</li>
<li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
<em>Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</em></p>

<pre><code>bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table &#39;holberton.users&#39; doesn&#39;t exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Jean&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry &#39;bob@dylan.com&#39; for key &#39;email&#39;
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>0-uniq_users.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11633">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11633" data-batch-id="80" data-toggle="modal" data-target="#task-11633-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11633-users-done-modal" data-task-id="11633" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "0. We are all unique!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11633-modal-button" data-task-id="11633" data-toggle="modal" data-target="#task-test-correction-11633-correction-modal" id="task-num-0-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11633}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11633-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. We are all unique!"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11633">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11633">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11633">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11633}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11634" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-11634">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. In and not out
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a table <code>users</code> following these requirements:</p>

<ul>
<li>With these attributes:

<ul>
<li><code>id</code>, integer, never null, auto increment and primary key</li>
<li><code>email</code>, string (255 characters), never null and unique</li>
<li><code>name</code>, string (255 characters)</li>
<li><code>country</code>, enumeration of countries: <code>US</code>, <code>CO</code> and <code>TN</code>, never null (= default will be the first element of the enumeration, here <code>US</code>)</li>
</ul></li>
<li>If the table already exists, your script should not fail</li>
<li>Your script can be executed on any database</li>
</ul>

<pre><code>bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table &#39;holberton.users&#39; doesn&#39;t exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;, &quot;US&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;, &quot;CO&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;jean@dylan.com&quot;, &quot;Jean&quot;, &quot;FR&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column &#39;country&#39; at row 1
bob@dylan:~$ 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;john@dylan.com&quot;, &quot;John&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>1-country_users.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11634">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11634" data-batch-id="80" data-toggle="modal" data-target="#task-11634-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11634-users-done-modal" data-task-id="11634" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "1. In and not out"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11634-modal-button" data-task-id="11634" data-toggle="modal" data-target="#task-test-correction-11634-correction-modal" id="task-num-1-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11634}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11634-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. In and not out"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11634">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11634">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11634">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11634}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11635" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-11635">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Best band ever!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip" target="_blank">metal_bands.sql.zip</a></li>
<li>Column names must be: <code>origin</code> and <code>nb_fans</code></li>
<li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
<em>Calculate/compute something is always power intensive&hellip; better to distribute the load!</em></p>

<pre><code>bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton &gt; tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>2-fans.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11635">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11635" data-batch-id="80" data-toggle="modal" data-target="#task-11635-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11635-users-done-modal" data-task-id="11635" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "2. Best band ever!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11635-modal-button" data-task-id="11635" data-toggle="modal" data-target="#task-test-correction-11635-correction-modal" id="task-num-2-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11635}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11635-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Best band ever!"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11635">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11635">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11635">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11635}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11636" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-11636">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Old school band
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that lists all bands with <code>Glam rock</code> as their main style, ranked by their longevity</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip" target="_blank">metal_bands.sql.zip</a></li>
<li>Column names must be: <code>band_name</code> and <code>lifespan</code> (in years <strong>until 2022</strong> - please use <code>2022</code> instead of <code>YEAR(CURDATE())</code>)</li>
<li>You should use attributes <code>formed</code> and <code>split</code> for computing the <code>lifespan</code></li>
<li>Your script can be executed on any database</li>
</ul>

<pre><code>bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>3-glam_rock.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11636">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11636" data-batch-id="80" data-toggle="modal" data-target="#task-11636-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11636-users-done-modal" data-task-id="11636" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "3. Old school band"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11636-modal-button" data-task-id="11636" data-toggle="modal" data-target="#task-test-correction-11636-correction-modal" id="task-num-3-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11636}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11636-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "3. Old school band"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11636">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11636">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11636">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11636}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11637" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-11637">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Buy buy buy
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.</p>

<p>Quantity in the table <code>items</code> can be negative.</p>

<p><strong>Context:</strong>
<em>Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc&hellip; to keep your data in a good shape, let MySQL do it for you!</em></p>

<pre><code>bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES (&quot;apple&quot;), (&quot;pineapple&quot;), (&quot;pear&quot;);

bob@dylan:~$ 
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql
Enter password: 
-- Show and add orders
SELECT * FROM items;
SELECT * FROM orders;

INSERT INTO orders (item_name, number) VALUES (&#39;apple&#39;, 1);
INSERT INTO orders (item_name, number) VALUES (&#39;apple&#39;, 3);
INSERT INTO orders (item_name, number) VALUES (&#39;pear&#39;, 2);

SELECT &quot;--&quot;;

SELECT * FROM items;
SELECT * FROM orders;

bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>4-store.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11637">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11637" data-batch-id="80" data-toggle="modal" data-target="#task-11637-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11637-users-done-modal" data-task-id="11637" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "4. Buy buy buy"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11637-modal-button" data-task-id="11637" data-toggle="modal" data-target="#task-test-correction-11637-correction-modal" id="task-num-4-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11637}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11637-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "4. Buy buy buy"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11637">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11637">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11637">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11637}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11638" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-11638">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Email validation to sent
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a trigger that resets the attribute <code>valid_email</code> only when the <code>email</code> has been changed.</p>

<p><strong>Context:</strong>
<em>Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!</em></p>

<pre><code>bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;);
INSERT INTO users (email, name, valid_email) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;, 1);
INSERT INTO users (email, name, valid_email) VALUES (&quot;jeanne@dylan.com&quot;, &quot;Jeanne&quot;, 1);

bob@dylan:~$ 
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql
Enter password: 
-- Show users and update (or not) email
SELECT * FROM users;

UPDATE users SET valid_email = 1 WHERE email = &quot;bob@dylan.com&quot;;
UPDATE users SET email = &quot;sylvie+new@dylan.com&quot; WHERE email = &quot;sylvie@dylan.com&quot;;
UPDATE users SET name = &quot;Jannis&quot; WHERE email = &quot;jeanne@dylan.com&quot;;

SELECT &quot;--&quot;;
SELECT * FROM users;

UPDATE users SET email = &quot;bob@dylan.com&quot; WHERE email = &quot;bob@dylan.com&quot;;

SELECT &quot;--&quot;;
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>5-valid_email.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11638">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11638" data-batch-id="80" data-toggle="modal" data-target="#task-11638-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11638-users-done-modal" data-task-id="11638" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "5. Email validation to sent"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11638-modal-button" data-task-id="11638" data-toggle="modal" data-target="#task-test-correction-11638-correction-modal" id="task-num-5-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11638}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11638-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "5. Email validation to sent"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11638">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11638">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11638">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11638}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11639" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-11639">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Add bonus
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a stored procedure <code>AddBonus</code> that adds a new correction for a student.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>AddBonus</code> is taking 3 inputs (in this order):

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
<li><code>project_name</code>, a new or already exists <code>projects</code> - if no <code>projects.name</code> found in the table, you should create it</li>
<li><code>score</code>, the score value for the correction</li>
</ul></li>
</ul>

<p><strong>Context:</strong>
<em>Write code in SQL is a nice level up!</em></p>

<pre><code>bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;C is fun&quot;);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;Python is cool&quot;);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql
Enter password: 
-- Show and add bonus correction
SELECT * FROM projects;
SELECT * FROM corrections;

SELECT &quot;--&quot;;

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;Python is cool&quot;, 100);

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;Bonus project&quot;, 100);
CALL AddBonus((SELECT id FROM users WHERE name = &quot;Bob&quot;), &quot;Bonus project&quot;, 10);

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;New bonus&quot;, 90);

SELECT &quot;--&quot;;

SELECT * FROM projects;
SELECT * FROM corrections;

bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name
1   C is fun
2   Python is cool
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>6-bonus.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11639">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11639" data-batch-id="80" data-toggle="modal" data-target="#task-11639-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11639-users-done-modal" data-task-id="11639" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "6. Add bonus"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11639-modal-button" data-task-id="11639" data-toggle="modal" data-target="#task-test-correction-11639-correction-modal" id="task-num-6-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11639}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11639-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "6. Add bonus"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11639">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11639">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11639">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11639}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11640" data-position="8" id="task-num-7">
      <div class="panel panel-default task-card " id="task-11640">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Average score
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a stored procedure <code>ComputeAverageScoreForUser</code> that computes and store the average score for a student.

Note: An average score can be a decimal</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>ComputeAverageScoreForUser</code> is taking 1 input:

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
</ul></li>
</ul>

<pre><code>bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;C is fun&quot;);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;Python is cool&quot;);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-average_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT * FROM users;
SELECT * FROM corrections;

SELECT &quot;--&quot;;
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = &quot;Jeanne&quot;));

SELECT &quot;--&quot;;
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>7-average_score.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11640">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11640" data-batch-id="80" data-toggle="modal" data-target="#task-11640-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11640-users-done-modal" data-task-id="11640" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "7. Average score"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11640-modal-button" data-task-id="11640" data-toggle="modal" data-target="#task-test-correction-11640-correction-modal" id="task-num-7-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11640}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11640-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "7. Average score"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11640">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11640">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11640">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11640}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11641" data-position="9" id="task-num-8">
      <div class="panel panel-default task-card " id="task-11641">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Optimize simple search
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates an index <code>idx_name_first</code> on the table <code>names</code> and the first letter of <code>name</code>.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip" target="_blank">names.sql.zip</a></li>
<li>Only the first letter of <code>name</code> must be indexed</li>
</ul>

<p><strong>Context:</strong>
<em>Index is not the solution for any performance issue, but well used, it&rsquo;s really powerful!</em></p>

<pre><code>bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39;;
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 8-index_my_names.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql&gt; 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39;;
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>8-index_my_names.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11641">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11641" data-batch-id="80" data-toggle="modal" data-target="#task-11641-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11641-users-done-modal" data-task-id="11641" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "8. Optimize simple search"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11641-modal-button" data-task-id="11641" data-toggle="modal" data-target="#task-test-correction-11641-correction-modal" id="task-num-8-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11641}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11641-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "8. Optimize simple search"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11641">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11641">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11641">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11641}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11642" data-position="10" id="task-num-9">
      <div class="panel panel-default task-card " id="task-11642">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Optimize search and score
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates an index <code>idx_name_first_score</code> on the table <code>names</code> and the first letter of <code>name</code> and the <code>score</code>.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip" target="_blank">names.sql.zip</a></li>
<li>Only the first letter of <code>name</code> AND <code>score</code> must be indexed</li>
</ul>

<pre><code>bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39; AND score &lt; 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 9-index_name_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name             | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx_name_first_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql&gt; 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39; AND score &lt; 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>9-index_name_score.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11642">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11642" data-batch-id="80" data-toggle="modal" data-target="#task-11642-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11642-users-done-modal" data-task-id="11642" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "9. Optimize search and score"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11642-modal-button" data-task-id="11642" data-toggle="modal" data-target="#task-test-correction-11642-correction-modal" id="task-num-9-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11642}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11642-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "9. Optimize search and score"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11642">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11642">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11642">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11642}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11643" data-position="11" id="task-num-10">
      <div class="panel panel-default task-card " id="task-11643">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Safe divide
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a function <code>SafeDiv</code> that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>You must create a function</li>
<li>The function <code>SafeDiv</code> takes 2 arguments:

<ul>
<li><code>a</code>, INT</li>
<li><code>b</code>, INT</li>
</ul></li>
<li>And returns <code>a / b</code> or 0 if <code>b == 0</code></li>
</ul>

<pre><code>bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT (a / b) FROM numbers;&quot; | mysql -uroot -p holberton
Enter password: 
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT SafeDiv(a, b) FROM numbers;&quot; | mysql -uroot -p holberton
Enter password: 
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>10-div.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11643">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11643" data-batch-id="80" data-toggle="modal" data-target="#task-11643-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11643-users-done-modal" data-task-id="11643" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "10. Safe divide"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11643-modal-button" data-task-id="11643" data-toggle="modal" data-target="#task-test-correction-11643-correction-modal" id="task-num-10-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11643}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11643-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "10. Safe divide"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11643">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11643">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11643">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11643}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11644" data-position="12" id="task-num-11">
      <div class="panel panel-default task-card " id="task-11644">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. No table for a meeting
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a view <code>need_meeting</code> that lists all students that have a score under 80 (strict) and no <code>last_meeting</code> or more than 1 month.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>The view <code>need_meeting</code> should return all students name when:

<ul>
<li>They score are under (strict) to 80</li>
<li><strong>AND</strong> no <code>last_meeting</code> date <strong>OR</strong> more than a month</li>
</ul></li>
</ul>

<pre><code>bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES (&quot;Bob&quot;, 80);
INSERT INTO students (name, score) VALUES (&quot;Sylvia&quot;, 120);
INSERT INTO students (name, score) VALUES (&quot;Jean&quot;, 60);
INSERT INTO students (name, score) VALUES (&quot;Steeve&quot;, 50);
INSERT INTO students (name, score) VALUES (&quot;Camilia&quot;, 80);
INSERT INTO students (name, score) VALUES (&quot;Alexa&quot;, 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-need_meeting.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET score = 40 WHERE name = &#39;Bob&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET score = 80 WHERE name = &#39;Steeve&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET last_meeting = CURDATE() WHERE name = &#39;Jean&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = &#39;Jean&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

SHOW CREATE TABLE need_meeting;

SELECT &quot;--&quot;;

SHOW CREATE TABLE students;

bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password: 
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character_set_client    collation_connection
XXXXXX&lt;yes, here it will display the View SQL statement :-) &gt;XXXXXX
--
--
Table   Create Table
students    CREATE TABLE `students` (\n  `name` varchar(255) NOT NULL,\n  `score` int(11) DEFAULT &#39;0&#39;,\n  `last_meeting` date DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>11-need_meeting.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11644">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11644" data-batch-id="80" data-toggle="modal" data-target="#task-11644-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11644-users-done-modal" data-task-id="11644" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "11. No table for a meeting"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11644-modal-button" data-task-id="11644" data-toggle="modal" data-target="#task-test-correction-11644-correction-modal" id="task-num-11-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11644}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11644-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "11. No table for a meeting"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11644">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11644">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11644">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11644}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11645" data-position="13" id="task-num-12">
      <div class="panel panel-default task-card " id="task-11645">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Average weighted score
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a stored procedure <code>ComputeAverageWeightedScoreForUser</code> that computes and store the average weighted score for a student.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>ComputeAverageScoreForUser</code> is taking 1 input:

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
</ul></li>
</ul>

<p><strong>Tips</strong>:</p>

<ul>
<li><a href="/rltoken/QHx92mlF43zF6GTEil-Cyw" title="Calculate-Weighted-Average" target="_blank">Calculate-Weighted-Average</a></li>
</ul>

<pre><code>bob@dylan:~$ cat 100-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    weight int default 1,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score float default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;C is fun&quot;, 1);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;Python is cool&quot;, 2);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 100-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 100-average_weighted_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 100-main.sql
-- Show and compute average weighted score
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE name = &quot;Jeanne&quot;));

SELECT &quot;--&quot;;
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 100-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  82
id  name    weight
1   C is fun    1
2   Python is cool  2
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
id  name    average_score
1   Bob 0
2   Jeanne  79
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>100-average_weighted_score.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11645">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11645" data-batch-id="80" data-toggle="modal" data-target="#task-11645-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11645-users-done-modal" data-task-id="11645" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "12. Average weighted score"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11645-modal-button" data-task-id="11645" data-toggle="modal" data-target="#task-test-correction-11645-correction-modal" id="task-num-12-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11645}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11645-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "12. Average weighted score"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11645">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11645">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11645">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11645}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
    <div data-role="task11646" data-position="14" id="task-num-13">
      <div class="panel panel-default task-card " id="task-11646">

<span id="user_id" data-id="343517"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      13. Average weighted score for all!
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="343517"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a SQL script that creates a stored procedure <code>ComputeAverageWeightedScoreForUsers</code> that computes and store the average weighted score for all students.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>ComputeAverageWeightedScoreForUsers</code> is not taking any input.</li>
</ul>

<p><strong>Tips</strong>:</p>

<ul>
<li><a href="/rltoken/QHx92mlF43zF6GTEil-Cyw" title="Calculate-Weighted-Average" target="_blank">Calculate-Weighted-Average</a></li>
</ul>

<pre><code>bob@dylan:~$ cat 101-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    weight int default 1,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score float default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;C is fun&quot;, 1);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES (&quot;Python is cool&quot;, 2);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 101-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 101-average_weighted_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 101-main.sql
-- Show and compute average weighted score
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL ComputeAverageWeightedScoreForUsers();

SELECT &quot;--&quot;;
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 101-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
id  name    weight
1   C is fun    1
2   Python is cool  2
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
id  name    average_score
1   Bob 90.6667
2   Jeanne  79
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-backend-storage</code></li>
            <li>Directory: <code>0x00-MySQL_Advanced</code></li>
            <li>File: <code>101-average_weighted_score.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11646">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11646" data-batch-id="80" data-toggle="modal" data-target="#task-11646-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-11646-users-done-modal" data-task-id="11646" data-batch-id="80">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "13. Average weighted score for all!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>

      <button class="btn btn-default btn-sm check-your-task-11646-modal-button" data-task-id="11646" data-toggle="modal" data-target="#task-test-correction-11646-correction-modal" id="task-num-13-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:11646}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11646-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "13. Average weighted score for all!"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11646">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11646">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11646">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>

</div>

            </div>
        </div>
    </div>

</div>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11646}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>

        <div class="fs-4">
        </div>
      </div>

  </div>
</div>

    </div>
          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;available&quot;:true,&quot;description&quot;:&quot;\u003cp\u003eUbuntu 18.04 with Python 3.7\u003c/p\u003e\n&quot;,&quot;id&quot;:23,&quot;name&quot;:&quot;Ubuntu 18.04 - Python 3.7&quot;,&quot;online&quot;:true}],&quot;containersLimit&quot;:2,&quot;csrfToken&quot;:&quot;6-oOnpF6Gi_wpt78zWRj6v4EqNuBeRa7mIipkKH-LzTVIGQWitOwf7Mk0pJJCF3ZmYIPg0ynbnMoLYh9UKgefA&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>

  </div>
</div>

      </article>

      <div class="copyright">Copyright © 2024 ALX, All rights reserved.</div>

    </main>

        <button class="btn btn-primary atop-zendesk" id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">

<i aria-hidden="true" class="fa-solid fa-magnifying-glass "></i>
<i aria-hidden="true" class="fa-solid fa-window-minimize "></i>
</button>

        <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            autocomplete="off"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">

</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">

</div>

            </div>
        </div>
    </div>

</div>

        <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">

  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

