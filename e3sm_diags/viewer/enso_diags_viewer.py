import os

from e3sm_diags.logger import _setup_child_logger
from e3sm_diags.parameter.enso_diags_parameter import EnsoDiagsParameter
from e3sm_diags.viewer.core_viewer import OutputViewer

from .default_viewer import create_metadata
from .utils import add_header, h1_to_h3

logger = _setup_child_logger(__name__)


def create_viewer(root_dir, parameters):
    """
    Given a set of parameters for the enso_diags set,
    create a single webpage.

    Return the title and url for this page.
    """
    viewer = OutputViewer(path=root_dir)

    # The name that's displayed on the viewer.
    display_name = "ENSO Diagnostics"
    set_name = "enso_diags"

    # The title of the colums on the webpage.
    # Appears in the second and third columns of the bolded rows.
    cols = ["Description", "Plot"]
    viewer.add_page(display_name, short_name=set_name, columns=cols)
    param_dict: dict[str, list[EnsoDiagsParameter]] = {}

    for param in parameters:
        key = param.plot_type

        if key not in param_dict.keys():
            param_dict[key] = []

        param_dict[key].append(param)

    for plot_type in param_dict.keys():
        # Appears in the first column of the bolded rows.
        viewer.add_group(plot_type.capitalize())
        # Only iterate through parameters with this plot type.
        valid_parameters = param_dict[plot_type]
        for param in valid_parameters:
            # We need to make sure we have relative paths, and not absolute ones.
            # This is why we don't use get_output_dir() as in the plotting script
            # to get the file name.
            ext = param.output_format[0]
            # param.output_file is defined in e3sm_diags/driver/enso_diags_driver.py
            # This must be use param.case_id and param.output_file
            # to match the file_path determined in
            # e3sm_diags/plot/cartopy/enso_diags_plot.py.
            # Otherwise, the plot will not be properly linked from the viewer.
            relative_path = os.path.join(
                "..", set_name, param.case_id, param.output_file
            )
            image_relative_path = "{}.{}".format(relative_path, ext)
            if param.print_statements:
                logger.info("image_relative_path: {}".format(image_relative_path))
            formatted_files = []
            if param.save_netcdf:
                nc_files = [
                    relative_path + nc_ext
                    for nc_ext in ["_test.nc", "_ref.nc", "_diff.nc"]
                ]
                formatted_files = [{"url": f, "title": f} for f in nc_files]
            # TODO: will param.variables ever be longer than one variable?
            #  If so, we'll need to create unique image_relative_paths
            for var in param.variables:
                # Appears in the first column of the non-bolded rows.
                # This should use param.case_id to match the output_dir determined by
                # get_output_dir in e3sm_diags/plot/cartopy/enso_diags_plot.py.
                # Otherwise, the plot image and the plot HTML file will have URLs
                # differing in the final directory name.
                viewer.add_row(param.case_id)
                # Adding the description for this var to the current row.
                # This was obtained and stored in the driver for this plotset.
                # Appears in the second column of the non-bolded rows.
                viewer.add_col(param.viewer_descr[var])
                # Link to an html version of the plot png file.
                # Appears in the third column of the non-bolded rows.
                viewer.add_col(
                    image_relative_path,
                    is_file=True,
                    title="Plot",
                    other_files=formatted_files,
                    meta=create_metadata(param),
                )

    url = viewer.generate_page()
    add_header(root_dir, os.path.join(root_dir, url), parameters)
    h1_to_h3(os.path.join(root_dir, url))

    return display_name, url
