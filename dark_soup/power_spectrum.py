import limpy.lines as ll
import limpy.powerspectra as lp
import limpy.params as p
import limpy.utils as lu
import limpy.plotter as lplt
import numpy as np


def get_ps_intensity_mapping(z, k_range=(-2, 1), line_name="CII158", model_name='Fonseca16', sfr_model='Silva15'):
    """Generate the power spectrum (k and pk) from intensity mapping with the halo model.

    Parameters
    ----------
    z : float
        The redshift.
    k_range : tuple of (int, int)
        The range of k to use.
    """

    k = np.logspace(*k_range, num=1000)
    pk_theory = ll.theory().Pk_line(
        k,
        z,
        line_name=line_name,
        model_name=model_name,
        label='total',
        pk_unit='intensity',
    )

    return k, pk_theory

def get_ps_point_sources(z, halo_file_path, line_name="CII158", model_name='Fonseca16', sfr_model='Silva15'):
    """Generate a power spectrum with point source data (the halo file).

    Parameters
    ----------
    z : float
        The redshift.
    halo_file_path: str
        The path to the npz halo file.
    line_name : str
        The spectrum line name.
    model_name : str
        The model to convert sfr to line luminosity.
    sfr_model : str
        Star formation rate model.
    """

    mmin = 1e11
    small_h = 0.68 # value of Hubble parameter. H0 = 100 * small_h
    ngrid= 256 # numer of grid points along the all three exes
    boxsize = 205 # Length of the box 

    sim = ll.lim_sims(
        halo_file_path,
        z,
        sfr_model=sfr_model,
        model_name=model_name,
        line_name=line_name,
        halo_cutoff_mass=mmin,
        halocat_type="input_cat",
        ngrid_x = ngrid, 
        ngrid_y = ngrid, 
        ngrid_z = ngrid, 
        boxsize_x=boxsize,
        boxsize_y=boxsize,
        boxsize_z=boxsize,
    )
    Ig = sim.make_intensity_grid()
    ngrid_new = np.shape(Ig)[2]
    kb, pkb = lp.get_pk3d(
        Ig,
        boxsize,
        boxsize,
        boxsize,
        ngrid,
        ngrid,
        ngrid_new,
    )

    return kb, pkb
