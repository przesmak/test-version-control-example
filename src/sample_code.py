def formulation_Custom(f_range, bb):
    #print("Using custom PSD")
    # load the dimensional PSD from     
    df=pd.read_excel('force-psds-custom.xlsx', sheet_name = 'Custom')
    freqs = pd.to_numeric(df['Frequency [Hz]'])
    if bb < 10:
        bendcolumn = 'b0' + str(bb+1)
    else:
        bendcolumn = 'b' + str(bb+1)
        
    psd = pd.to_numeric(df[bendcolumn])
    
    Frms = np.sqrt(np.trapz(psd,x=freqs))
    
    df = f_range[-1] - f_range[-2]
    
    freqlimit = (f_range[-1] + 20.)
    if freqs.iloc[-1] < freqlimit:
        a = np.arange(freqs.iloc[-1], (f_range[-1] + 20.), df)
        b = np.zeros_like(a)
        fi = np.hstack((freqs,a))
        psdi = np.hstack((psd,b))
    else:
        fi = freqs
        psdi = psd

    func = interpolate.interp1d(fi, psdi)
    #fr = np.arange(df, f_range[-1], df)
    phi = func(f_range)
    # fig = plt.figure()
    # plt.plot(fi,psdi,'-',f_range,phi,'o')
    # plt.xlim([0, 200]) 
    # plt.show()
    # fig.savefig('psdinterp-check'+bendcolumn+'.png')
    
    return (Frms, phi)