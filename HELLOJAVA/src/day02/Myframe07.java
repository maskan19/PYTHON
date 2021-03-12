package day02;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class Myframe07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfCom;
	private JTextField tfMine;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Myframe07 frame = new Myframe07();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Myframe07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lblCom = new JLabel("\uCEF4: ");
		lblCom.setBounds(25, 30, 57, 15);
		contentPane.add(lblCom);

		JLabel lblMine = new JLabel("\uB098:");
		lblMine.setBounds(25, 83, 57, 15);
		contentPane.add(lblMine);

		tfCom = new JTextField();
		tfCom.setText("");
		tfCom.setBounds(114, 27, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);

		tfMine = new JTextField();
		tfMine.setText("");
		tfMine.setBounds(114, 80, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);

		JLabel lblResult = new JLabel("\uACB0\uACFC: ");
		lblResult.setBounds(25, 134, 57, 15);
		contentPane.add(lblResult);

		tfResult = new JTextField();
		tfResult.setBounds(114, 131, 116, 21);
		contentPane.add(tfResult);
		tfResult.setColumns(10);

		JButton btn = new JButton("\uC2E4\uD589\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String com = Math.random() > 0.5 ? "È¦" : "Â¦";
				tfCom.setText(com);
				String mine = tfMine.getText();
				String result = com.equals(mine) ? "½Â¸®" : "ÆÐ¹è";
				tfResult.setText(result);
			}
		});
		btn.setBounds(12, 180, 97, 23);
		contentPane.add(btn);
	}

}
