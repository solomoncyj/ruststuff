let spec = ls *.spec
rm ~/rpmbuild/SRPMS/*  /home/solomoncyj/rpmbuild/SOURCES/* -f
cp ./*.diff /home/solomoncyj/rpmbuild/SOURCES/
$spec.name | each {|in|
    print $"processing ($in)"
    let url = (spectool $in)
        |str replace "Source0:" ""
    let name = $url | path basename
    http get $url | save $"/home/solomoncyj/rpmbuild/SOURCES/($name)"
    rpmbuild -bs $in
    }
cp '~/rpmbuild/SRPMS/' .