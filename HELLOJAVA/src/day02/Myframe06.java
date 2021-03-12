package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Myframe06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfDan;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Myframe06 frame = new Myframe06();
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
	public Myframe06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tfDan = new JTextField();
		tfDan.setText("2");
		tfDan.setBounds(290, 49, 85, 21);
		contentPane.add(tfDan);
		tfDan.setColumns(10);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(12, 10, 235, 241);
		contentPane.add(ta);
		
		JButton btn = new JButton("\uCD9C\uB825");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int dan = Integer.parseInt(tfDan.getText());
				ta.setText(dan + "* 1 = " + dan*1 + "\n" + 
						dan + "* 2 = " + dan*2 + "\n" + 
						dan + "* 3 = " + dan*3 + "\n" + 
						dan + "* 4 = " + dan*4 + "\n" + 
						dan + "* 5 = " + dan*5 + "\n" + 
						dan + "* 6 = " + dan*6 + "\n" + 
						dan + "* 7 = " + dan*7 + "\n" + 
						dan + "* 8 = " + dan*8 + "\n" + 
						dan + "* 9 = " + dan*9 + "\n");
				
			}
		});
		btn.setBounds(290, 88, 85, 23);
		contentPane.add(btn);
	}

}
